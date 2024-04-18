import ReloadIcon from './icons/ReloadIcon'

export default function Button({onClick, className, isLoading = false, children}) {
    return(
        <button className={`bg-[#A52A2A] py-2 px-3 rounded-md my-3 flex flex-row items-center ${className}`} onClick={onClick}>
            {
                isLoading ? (
                    <>
                        <ReloadIcon className="animate-spin"/>
                        <span className="block mx-2">Loading...</span>
                    </>
                ) : children
            }
        </button>
    )
}