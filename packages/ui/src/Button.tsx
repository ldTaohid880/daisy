import type { ButtonHTMLAttributes } from 'react';
import styles from './Button.module.css';

type Kind = 'primary' | 'secondary' | 'ghost' | 'danger';

export function Button({
  kind = 'secondary',
  className,
  ...rest
}: ButtonHTMLAttributes<HTMLButtonElement> & { kind?: Kind }) {
  return (
    <button
      type="button"
      className={[styles.button, styles[kind], className].filter(Boolean).join(' ')}
      {...rest}
    />
  );
}
