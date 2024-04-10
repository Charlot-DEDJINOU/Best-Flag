import { useState } from "react"
import { useNavigate } from 'react-router-dom'
import { login } from "../services/authService"
import Button from "../components/Button"
import Input from "../components/Input"
import AlertDanger from "../components/AlertDanger"
import AlertSuccess from "../components/AlertSuccess"

export default function Ascii() {

    const navigate = useNavigate()
    const [formData, setFormData] = useState({
        username : '',
        password : ''
    })
    const [message, setMessage] = useState({
        display : false,
        type : 'success',
        content : ''
    })

    const onChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };    

    const onSubmit = async (e) => {
        e.preventDefault();
        if (formData.username === '' || formData.password === '') {
            setMessage({
                display: true,
                type: 'error',
                content: 'Veuillez remplir tous les champs'
            });
        } else {
            const status = await login(formData);
            if (status == 200) {
                setMessage({
                    display: true,
                    type: 'success',
                    content: 'Connexion réussie avec succès'
                });
            } else if (status == 401) {
                setMessage({
                    display: true,
                    type: 'error',
                    content: 'Identifiants incorrects'
                });
            } else {
                setMessage({
                    display: true,
                    type: 'error',
                    content: 'Une erreur s\'est produite. Veuillez réessayer plus tard'
                });
            }
        }
    };
    
    return(
        <section id="ascii" className="w-full min-h-[47.5vh]">
            <div className="container m-auto flex flex-col items-center text-justify px-4">
                <p className="text-2xl font-medium mb-5">Algorithme ASCII</p>
                <p className="mb-3">
                    La clé que vous trouverez à cette étape est pour l'algorithme ascii. Et si on commençait par <b className="text-[#A52A2A]">se connecter</b> ?
                </p>
                <form className="w-80 lg:w-3/4" onSubmit={onSubmit}>
                    <Input
                        label="Nom d'utilisateur"
                        type="text"
                        placeholder="Charlot DEDJINOU"
                        name="username"
                        onChange={onChange}
                    />
                    <Input
                        label="Mot de passe"
                        type="password"
                        name="password"
                        onChange={onChange}
                    />
                    { message.display && message.type === 'error' && <AlertDanger message={message.content} /> }
                    { message.display && message.type === 'success' && <AlertSuccess message={message.content} /> }
                    <Button>Se connecter</Button>
                </form>
                <div className="flex flex-row justify-around w-96">
                    <Button onClick={() => navigate('/')}>Précédente</Button>
                    <Button onClick={() => navigate('/ascii')}>Suivante</Button>
                </div>
            </div>
        </section>
    )
}