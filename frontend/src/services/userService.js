import api from './api';

export const fetchUserData = async () => {
    const token = localStorage.getItem('token');
    if (!token) {
        throw new Error('Token non trouvé. Veuillez vous connecter.');
    }

    try {
        const response = await api.get('/user', {
            headers: {
                Authorization: token,
            },
        });
        return response.data;
    } catch (error) {
        throw new Error(error.response.data.message);
    }
};