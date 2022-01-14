import React from 'react'

const Button = (handleChange) => {

    const changeUsers = handleChange.handleChange

    return (
        <button className='border rounded-md w-64 h-12 hover:bg-purple' onClick={changeUsers}>
          Mostrar outros usuários  
        </button>
    )
}

export default Button
