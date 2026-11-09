import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';

type CardProps = {
  title: string;
  to: string;
  children?: ReactNode;
};

export function Card({title, to, children}: CardProps): ReactNode {
  return (
    <Link className={styles.card} to={to}>
      <span className={styles.title}>{title}</span>
      {children && <span className={styles.body}>{children}</span>}
    </Link>
  );
}

export function Cards({children}: {children: ReactNode}): ReactNode {
  return <div className={styles.grid}>{children}</div>;
}
