import NextAuth, { AuthOptions } from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';
import api from '../../../services/api'; // Adjust path if needed

export const authOptions: AuthOptions = {
  providers: [
    CredentialsProvider({
      name: 'Credentials',
      credentials: {
        email: { label: 'Email', type: 'email', placeholder: 'jsmith@example.com' },
        password: { label: 'Password', type: 'password' }
      },
      async authorize(credentials) {
        try {
          const response = await api.post('/users/login', { // Your login endpoint
            email: credentials?.email,
            password: credentials?.password,
          });

          if (response.status === 200) {
            const user = response.data;
            // Store any necessary user data in the session (e.g., token, user ID)
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
  // ... other NextAuth.js configurations (e.g., session, callbacks) ...
};

export default NextAuth(authOptions);
