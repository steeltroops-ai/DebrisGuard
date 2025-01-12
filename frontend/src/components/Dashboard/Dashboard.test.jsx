// frontend/src/components/Dashboard/Dashboard.test.jsx
import { render, screen } from '@testing-library/react';
import { Dashboard } from './Dashboard';

test('renders dashboard component', () => {
  render(<Dashboard />);
  expect(screen.getByTestId('debris-map')).toBeInTheDocument();
});