import React from "react";


const UsersItem = ({user}) =>{

    return(
    <tr>
        <td>
            {user.username}
        </td>
        <td>
            {user.first_name}
        </td>
        <td>
            {user.last_name}
        </td>
        <td>
            {user.email}
        </td>
    </tr>
    )
}

const UserList = ({users})=>{
    return(
    <table>
        <th>
            User name
        </th>
        <th>
            First_name
        </th>
        <th>
            Last_name
        </th>
        <th>
            E-mail
        </th>
        {users.map((user)=><UsersItem user={user}/>)}
    </table>
    )
}

export default UserList;