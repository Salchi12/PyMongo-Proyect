import React, {useState} from 'react';

const API=process.env.REACT_APP_BACKEND;

export const Users = () => {
    
    const [username,setName] = useState('')
    const [email,setEmail] = useState('')
    const [password,setPassword] = useState('')


    const handleSubmit = async (e) => {
        e.preventDefault();
        const response=await fetch(`${API}/user`, { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username,
                email,
                password
            })
        })
        const data=await response.json();
        console.log(data)
    }
    return (
        <div className="row">
            <div className="col-md-4">
                <form onSubmit={handleSubmit}className=" card card-body">
                    <div className="form-group">
                        <input type="text" 
                        onChange={e=>setName(e.target.value)} 
                        value={username}
                        className="form-control"
                        placeholder="UserName"
                        autoFocus
                        />
                    </div>
                    <div className="form-group">
                        <input type="email" 
                        onChange={e=>setEmail(e.target.value)} 
                        value={email}
                        className="form-control"
                        placeholder="Email"
                        />
                    </div>
                    <div className="form-group">
                        <input type="password" 
                        onChange={e=>setPassword(e.target.value)} 
                        value={password}
                        className="form-control"
                        placeholder="Password"
                        />
                    </div>
                    <button className="btn btn-primary btn-block">
                        Register
                    </button>
                </form>
            </div>


        </div>
    )

}