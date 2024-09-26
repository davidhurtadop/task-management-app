import AuthForm from '../components/AuthForm';
import { useRouter } from 'next/navigation';

const LoginPage = () => {
  const router = useRouter();

  const handleAuthSuccess = () => {
    router.push('/tasks');
  };

  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: '100vh',
      }}
    >
      <AuthForm onAuthSuccess={handleAuthSuccess} />
    </div>
  );
};

export default LoginPage;
