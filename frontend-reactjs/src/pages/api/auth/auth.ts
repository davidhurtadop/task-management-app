import NextAuth, { AuthOptions } from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';

export const authOptions: AuthOptions = {
  providers: [
    CredentialsProvider({
      name: 'Credentials',
      credentials: {
        email: { label: 'Email', type: 'email', placeholder: 'jsmith@example.com' },
        password: { label: 'Password', type: 'password' }
      },
      async authorize(credentials) {
        if (!credentials?.email || !credentials?.password) {
          return null;
        }

        try {
          const res = await fetch('http://localhost:5000/api/login', { // Replace with your API endpoint
            method: 'POST',
            body: JSON.stringify(credentials),
            headers: { 'Content-Type': 'application/json' },
          });

          if (res.ok) {
            const user = await res.json();
            return user;
          } else {
            throw new Error('Invalid credentials');
          }
        } catch (error) {
          throw new Error('An error occurred during authentication.');
        }
      },
    }),
  ],
  // ... other NextAuth.js configurations ...
};

export default NextAuth(authOptions);
