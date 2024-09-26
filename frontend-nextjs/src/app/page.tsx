"use client";
import Image from 'next/image';
import AuthForm from '../components/AuthForm';
import { useRouter } from 'next/navigation';

export default function Home() {
  const router = useRouter();

  const handleAuthSuccess = () => {
    router.push('/tasks');
  };

  return (
    <main
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: '100vh',
      }}
    >
      <AuthForm onAuthSuccess={handleAuthSuccess} />
    </main>
  );
}
