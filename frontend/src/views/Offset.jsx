import Button from "../components/Button"
import { useNavigate } from 'react-router-dom'
import ReloadIcon from "../components/icons/ReloadIcon"
import { OffsetData } from "../data/OffsetData"
import CheckIcon from "../components/icons/CheckIcon"
import DeniedIcon from "../components/icons/DeniedIcon"
import { getAuthorization } from "../services/cryptService"
import { useEffect, useState } from "react"

export default function Offset() {

    const navigate = useNavigate()
    
    const [message, setMessage] = useState({
        authorization : [false,false,false,false],
        content : ""
    })

    const [loading, setLoading] = useState(false)

    const offset = async () => {
        setLoading(true)
        const response = await getAuthorization()
        setLoading(false)
       
        if(response.authorization) {
            setMessage({
                authorization : response.authorization,
                content : response.message
            })
        }else if(response.status === 401) {
            setMessage({
                authorization : [false, message.authorization[1], message.authorization[2], message.authorization[3]],
                content : response.message
            })
        } else {
            setMessage({
                authorization : message.authorization,
                content : response.message
            })
        }
    }

    useEffect(() => { offset(); }, []);

    return(
        <section id="offset" className="w-full">
            <div className="container m-auto flex flex-col items-center text-justify px-4">
                <p className="text-2xl font-medium mb-5">Algorithme OFFSET</p>
                <p className="mb-3">
                    La clé que vous trouverez à cette étape est pour l'algorithme offset. Et si on commençait par <b className="text-[#A52A2A]">se donner des droits</b> ?
                </p>
                <div className="w-full min-h-[100px] my-5 flex-wrap flex justify-between">
                    <div>
                        <Button className='flex flex-row items-center mb-5' onClick={offset} isLoading={loading}>
                            <ReloadIcon /> 
                            <span className="block mx-2">Recharger</span>
                        </Button>
                        {
                            OffsetData().map((item, index) => (
                                <div className="flex my-2" key={index}>
                                    {message.authorization[index] ? <CheckIcon /> : <DeniedIcon />}
                                    <span className="mx-2">{item}</span>
                                </div>
                            ))
                        }
                    </div>
                    <div className="flex flex-col items-start">
                        <Button onClick={null} className="mb-5">
                            Message pour les administateurs
                        </Button>
                        <p>
                            Vous devez remplir les 04 conditions avant de lire ce message<br /><br />
                            <span className="text-[#A52A2A] font-bold">Message : </span>{message.content}
                        </p>
                    </div>
                </div>
                <div className="flex flex-row justify-around w-96">
                    <Button onClick={() => navigate('/aes')}>Précédente</Button>
                    <Button onClick={() => navigate('/rotn')}>Suivante</Button>
                </div>
            </div>
        </section>
    )
}