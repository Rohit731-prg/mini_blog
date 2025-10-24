import { create } from 'zustand';
import toast from 'react-hot-toast';
import { axiosInstance } from '../Utils/axios';

const useUserStore = create((set, get) => ({
    user: null,

    login: async (user) => {
        console.log(user);
        try {
            const res = await toast.promise(
                axiosInstance.post("http://localhost:4000/user/login", user),
                {
                    loading: 'Loading...',
                    success: (res) => {
                        set({ user: res.data.user });
                        return res.data.message || 'Login successful';
                    },
                    error: (err) => err?.response?.data?.detail || 'Login failed',
                }
            );
            // const apiCall = axiosInstance.post("http://localhost:4000/user/login", user);
            // apiCall.then(res => console.log(res)).catch(err => console.error(err));


            return true;
        } catch (error) {
            console.error('Login error:', error);
        }
    }
}));

export default useUserStore;
