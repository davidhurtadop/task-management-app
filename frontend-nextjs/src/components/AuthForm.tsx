"use client";

import React, { useState } from 'react';
import { Button, Input, Spacer } from '@nextui-org/react';
import api from '../services/api';
import { useRouter } from 'next/navigation';
import { MailIcon } from '../styles/MailIcon';
import {EyeFilledIcon} from "../styles/EyeFilledIcon";
import {EyeSlashFilledIcon} from "../styles/EyeSlashFilledIcon";

interface AuthFormProps {
  onAuthSuccess: () => void;
}

const AuthForm: React.FC<AuthFormProps> = ({ onAuthSuccess }) => {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter();

  const [isVisible, setIsVisible] = React.useState(false);

  const toggleVisibility = () => setIsVisible(!isVisible);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      const endpoint = isLogin ? '/auth/login' : '/auth/signup';
      const response = await api.post(endpoint, { email, password });

      if (response.status === 200) {
        // Assuming your API returns a token on successful login/signup
        const token = response.data.token;
        localStorage.setItem('token', token);
        onAuthSuccess(); // Notify parent component about successful auth
        router.push('/tasks'); // Redirect to the tasks page
      } else {
        console.error('Authentication failed:', response.data);
        // Handle authentication error (e.g., display error message)
      }
    } catch (error) {
      console.error('An error occurred during authentication:', error);
      // Handle network or other errors
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen">
      <form 
        onSubmit={handleSubmit}
        className="p-8 rounded-lg shadow-md w-96"
      >
        <h2 className="text-2xl font-bold text-center mb-6">
          {isLogin ? 'Login' : 'Sign Up'}
        </h2>

        <div className="mb-4"> {/* Email Input */}
          <Input
            isClearable
            type="email"
            label="Email"
            variant="bordered"
            placeholder="Enter your email"
            defaultValue="my-email@encora.com"
            onChange={(e) => setEmail(e.target.value)}
            onClear={() => console.log("input cleared")}
            startContent={
              <MailIcon className="text-2xl text-gray-400 pointer-events-none" />
            }
            className="w-full" 
          />
        </div>

        <div className="mb-4"> {/* Password Input */}
          <Input
            placeholder="Enter your password"
            label="Password"
            variant="bordered"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            endContent={
              <button 
                className="focus:outline-none" 
                type="button" 
                onClick={toggleVisibility} 
                aria-label="toggle password visibility"
              >
                {isVisible ? (
                  <EyeSlashFilledIcon className="text-2xl text-gray-400 pointer-events-none" />
                ) : (
                  <EyeFilledIcon className="text-2xl text-gray-400 pointer-events-none" />
                )}
              </button>
            }
            type={isVisible ? "text" : "password"}
            className="w-full" 
            required
          />
        </div>

        <Button type="submit" color="primary" className="w-full"> {/* Submit Button */}
          {isLogin ? 'Login' : 'Sign Up'}
        </Button>

        <Spacer y={5} /> {/* Use Spacer from NextUI or replace with Tailwind margin */}

        <p className="text-center"> {/* Toggle Login/Signup Link */}
          {isLogin ? "Don't have an account?   " : "Already have an account?   "}
          <a 
            href="#" 
            onClick={() => setIsLogin(!isLogin)}
            className="text-blue-500 hover:underline"
          >
            {isLogin ? 'Sign Up' : 'Login'}
          </a>
        </p>
      </form>
    </div>
  );
};

export default AuthForm;
