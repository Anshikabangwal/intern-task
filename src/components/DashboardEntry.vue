<template>
    <div class="max-w-4xl mx-auto mt-10 p-6 bg-white rounded shadow-md">
      <h2 class="text-2xl font-semibold mb-4">Dashboard</h2>
      <p class="mb-6">Welcome to your dashboard!</p>
      
      <button @click="logout" class="px-4 py-2 bg-red-600 border border-transparent rounded-md shadow-sm text-sm font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
        Logout
      </button>
    </div>
  </template>
  
  <script>

  import { useRouter } from 'vue-router';
  
  export default {
    setup() {
      const router = useRouter();
  
      const logout = () => {
        // Redirect to login page
        router.push('/login');
      };
  
      return {
        logout
      };
    }
  };
  </script>
  

  