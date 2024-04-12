import api from './api';

export const login = async (credentials) => {
    try {
        const response = await api.post('/login', credentials);
        if(response.status == 200) {
            const { token, user } = response.data;
            localStorage.setItem('token', token);
            localStorage.setItem('user', JSON.stringify({
                username : user.username,
                session : user._id
            }));
        }
        return response.status ;
    } catch (error) {
        localStorage.clear()
        return error.response.status ;
    }
};

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

export const fetchAsciiKey = async () => {

    const token = localStorage.getItem('token');
    if (!token) {
        throw new Error('Token non trouvé. Veuillez vous connecter.');
    }

    try {
        const response = await api.get('/ascii', {
            headers: {
                Authorization: token,
            },
        });
        const { key } = response.data;
        localStorage.setItem("key", key)
        return response.status;
    } catch (error) {
        localStorage.clear()
        return error.response.status ;
    }
};