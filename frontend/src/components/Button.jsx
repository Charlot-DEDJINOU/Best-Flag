export default function Button({onClick, className, children}) {
    return(
        <button className={`bg-[#A52A2A] py-2 px-3 rounded-md my-3 ${className}`} onClick={onClick}>{ children }</button>
    )
}