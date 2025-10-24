import React, { useState } from 'react';
import useUserStore from '../store/UserStore';
import { Toaster } from "react-hot-toast"

export default function Login() {
    const { login } = useUserStore();
    const [userDetails, setUserDetails] = useState({
        email: '',
        password: ''
    });

    const handelSubmit = async (e) => {
        e.preventDefault();
        const res = await login(userDetails);
        // console.log(res);
    }
  return (
    <main className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      <div className="bg-white shadow-lg rounded-2xl p-8 w-full max-w-md">
        <h2 className="text-2xl font-semibold text-center mb-6">Login</h2>
        <form className="space-y-4" onSubmit={handelSubmit}>
          <div>
            <label className="block mb-1 font-medium">Email</label>
            <input
              value={userDetails.email}
              onChange={(e) => setUserDetails({ ...userDetails, email: e.target.value})}
              type="email"
              placeholder="Enter your email"
              className="w-full p-3 border rounded-lg focus:outline-none focus:ring"
            />
          </div>
          <div>
            <label className="block mb-1 font-medium">Password</label>
            <input
                onChange={(e) => setUserDetails({ ...userDetails, password: e.target.value})}
              type="password"
              placeholder="Enter your password"
              className="w-full p-3 border rounded-lg focus:outline-none focus:ring"
            />
          </div>
          <button
            type="submit"
            className="w-full py-3 rounded-lg font-semibold bg-blue-600 text-white hover:bg-blue-700"
          >
            Login
          </button>
        </form>
      </div>
      <Toaster />
    </main>
  );
}
