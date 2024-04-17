import axios from 'axios';

const api = axios.create({
    baseURL: 'https://best-flag.onrender.com/api', 
});

export default api;