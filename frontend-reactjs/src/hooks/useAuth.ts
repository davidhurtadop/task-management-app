import { useContext } from 'react';
import { AuthContext } from '../context/AuthContext';

export const useAuth = () => {
  const { token, login, logout } = useContext(AuthContext);
  return { token, login, logout };
};
