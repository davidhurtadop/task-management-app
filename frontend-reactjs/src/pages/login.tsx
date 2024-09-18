import { useState } from 'react';
import { useRouter } from 'next/router';
import axios from 'axios';
import { Input, Button, Spacer, Text } from '@nextui-org/react';

const LoginForm: React.FC = () => {
  const router = useRouter();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    try {
      const response = await axios.post('/api/users/login', { email, password });
      console.log('Login successful:', response.data);
      router.push('/'); 
    } catch (err: any) { 
      setError(err.response?.data?.message || 'An error occurred.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <Text h2>Login</Text>
      <Spacer y={1} />
      <Input 
        label="Email" 
        type="email" 
        value={email} 
        onChange={(e) => setEmail(e.target.value)} 
      />
      <Spacer y={1} />
      <Input 
        label="Password" 
        type="password" 
        value={password} 
        onChange={(e) => setPassword(e.target.value)} 
      />
      <Spacer y={1.5} />
      <Button type="submit">Login</Button>
      {error && <Text color="error" css={{ mt: '$5' }}>{error}</Text>}
    </form>
  );
};

export default LoginForm;
