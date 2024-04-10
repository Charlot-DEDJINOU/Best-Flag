import React from 'react';

export default function Input ({ label, type, name, placeholder, onChange }) {
  return (
    <div className='w-full mb-3 flex flex-col'>
        <label className='mb-1'>{label}</label>
        <input
            name={name}
            type={type}
            placeholder={placeholder}
            onChange={onChange}
            className="w-full px-4 py-2 rounded-md border text-black border-gray-300 focus:outline-none focus:border-[#A52A2A]"
        />
    </div>
  );
};