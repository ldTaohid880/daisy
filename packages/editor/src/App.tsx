import { Button } from '@daisy/ui';
import { useEffect, useState } from 'react';
import { useService } from './react/ContainerContext.js';
import { EditorTokens } from './tokens.js';

// Design: D-01 Home (placeholder until M03). The real shell is D-03/D-04 (M01).
export function App() {
  const versions = useService(EditorTokens.VersionService);
  const [label, setLabel] = useState('Starting…');
  useEffect(() => {
    void versions.label().then(setLabel);
  }, [versions]);
  return (
    <main
      style={{
        display: 'grid',
        placeItems: 'center',
        height: '100vh',
        background: 'var(--bg-workspace)',
        color: 'var(--text)',
      }}
    >
      <div style={{ textAlign: 'center' }}>
        <h1 style={{ font: '600 20px var(--font-ui)' }}>Daisy</h1>
        <p style={{ color: 'var(--text-muted)' }}>{label}</p>
        <Button kind="primary">New project</Button>
      </div>
    </main>
  );
}
