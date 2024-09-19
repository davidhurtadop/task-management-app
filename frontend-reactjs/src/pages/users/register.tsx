import RegisterForm from '../../components/auth/RegisterForm';

export default function RegisterPage() {
  return (
    <div className="container mx-auto py-10">
      <h1 className="text-2xl font-bold">Register</h1>
      <RegisterForm />
    </div>
  );
}