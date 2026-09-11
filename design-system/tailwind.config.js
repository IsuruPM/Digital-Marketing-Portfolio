/** Soft Ground — Tailwind theme extension v1.0 */
module.exports = {
  theme: {
    extend: {
      colors: {
        ground: '#F1F0EE',
        surface: '#FFFFFF',
        sunk: '#EAE8E5',
        hairline: '#E4E2DF',
        ink: { DEFAULT: '#17191B', 2: '#5F6367', 3: '#8E9296' },
        action: '#101214',
        tint: {
          mint: '#E3EDE4',
          sage: '#E9EDE8',
          blush: '#F8E7E2',
          cream: '#F7F0DF',
          mist: '#E4EBF3',
        },
      },
      fontFamily: {
        display: ['"Hanken Grotesk"', '"Helvetica Neue"', 'Arial', 'sans-serif'],
        sans: ['"Instrument Sans"', '"Helvetica Neue"', 'Arial', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
      fontSize: {
        'display-1': ['68px', { lineHeight: '1.04', letterSpacing: '-0.028em', fontWeight: '300' }],
        'display-2': ['44px', { lineHeight: '1.10', letterSpacing: '-0.024em', fontWeight: '300' }],
        'heading-1': ['32px', { lineHeight: '1.15', letterSpacing: '-0.020em', fontWeight: '300' }],
        'heading-2': ['22px', { lineHeight: '1.25', letterSpacing: '-0.014em', fontWeight: '400' }],
        'heading-3': ['17px', { lineHeight: '1.35', letterSpacing: '-0.008em', fontWeight: '500' }],
        body: ['15px', { lineHeight: '1.65' }],
        'body-sm': ['13px', { lineHeight: '1.60' }],
        eyebrow: ['11px', { lineHeight: '1.40', letterSpacing: '0.12em', fontWeight: '500' }],
        metric: ['44px', { lineHeight: '1', letterSpacing: '-0.03em', fontWeight: '300' }],
      },
      spacing: { section: '128px', 'section-sm': '64px', gutter: '24px' },
      maxWidth: { container: '1180px' },
      borderRadius: { sm: '4px', DEFAULT: '8px', md: '8px', lg: '12px', pill: '999px' },
      boxShadow: { lift: '0 8px 24px rgba(20,22,24,.06)' },
      transitionTimingFunction: { sg: 'cubic-bezier(.2,.7,.3,1)' },
      transitionDuration: { hover: '180ms', reveal: '420ms' },
    },
  },
};
