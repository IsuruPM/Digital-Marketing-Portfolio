<?php
// Inquiry form handler for plain PHP shared hosting (cPanel, Plesk, etc.).
// Sends each submission to the address below using the server's mail() function.
// Returns JSON for the site's JavaScript, or redirects to thanks.html without JavaScript.

$to      = 'hello@isurumarasinghe.com';
$subject = 'Website inquiry';
// Some hosts only deliver mail sent "from" an address on your own domain.
// If replies never arrive, set this to something like 'no-reply@yourdomain.com'.
$from    = '';

header('X-Content-Type-Options: nosniff');
$wantsJson = isset($_SERVER['HTTP_ACCEPT']) && strpos($_SERVER['HTTP_ACCEPT'], 'application/json') !== false;

function respond($ok, $message, $wantsJson) {
  if ($wantsJson) {
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode(['ok' => $ok, 'message' => $message]);
  } else {
    header('Location: ' . ($ok ? 'thanks.html' : 'index.html#contact'));
  }
  exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { respond(false, 'Method not allowed', $wantsJson); }
if (!empty($_POST['bot-field'])) { respond(true, 'ok', $wantsJson); } // honeypot: pretend success

$clean = function ($key, $max) {
  $v = isset($_POST[$key]) ? trim((string) $_POST[$key]) : '';
  $v = preg_replace('/[\x00-\x1F\x7F]/u', ' ', $v);   // every control char, not just CR and LF
  return mb_substr($v, 0, $max);
};
$name    = $clean('name', 120);
$email   = $clean('email', 200);
$phone   = $clean('phone', 60);
// JavaScript joins the dialling code to the number before posting; without it the two
// arrive separately, so put them back together here rather than losing the code.
$dial    = $clean('dial', 8);
if ($dial !== '' && strpos($phone, '+') !== 0) {
    $phone = $dial . ' ' . ltrim($phone, '0');
}
$inquiry = isset($_POST['inquiry']) ? mb_substr(trim((string) $_POST['inquiry']), 0, 5000) : '';

if ($name === '' || $phone === '' || $inquiry === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
  respond(false, 'Please complete every field with a valid email address.', $wantsJson);
}

$body  = "New inquiry from the website\n\n";
$body .= "Name:           $name\n";
$body .= "Email:          $email\n";
$body .= "Contact number: $phone\n";
$body .= "Sent:           " . date('Y-m-d H:i:s T') . "\n";
$body .= "IP:             " . ($_SERVER['REMOTE_ADDR'] ?? '') . "\n\n";
$body .= "Inquiry:\n$inquiry\n";

// SERVER_NAME can come straight from the Host header on some configurations, so it is
// never trusted into a mail header: anything but a plain hostname is discarded.
$host = (string) ($_SERVER['SERVER_NAME'] ?? '');
$host = preg_replace('/^www\./', '', $host);
if (!preg_match('/^[A-Za-z0-9.-]{1,253}$/', $host)) { $host = 'localhost'; }
$fromAddr = $from !== '' ? $from : ('no-reply@' . $host);
$headers  = "From: Website inquiry <$fromAddr>\r\n";
$headers .= "Reply-To: $name <$email>\r\n";
$headers .= "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\n";

$sent = @mail($to, $subject . ' from ' . $name, $body, $headers);
respond((bool) $sent, $sent ? 'sent' : 'The server could not send the email.', $wantsJson);
