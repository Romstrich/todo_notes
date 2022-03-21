import React from "react";


const AuthorItem = ({author}) =>{

    return(
    <tr>
        <td>
            {author.first_name}
        </td>
        <td>
            {author.last_name}
        </td>
        <td>
            {author.birthdate}
        </td>
    </tr>
    )
}

const AuthorList = ({authors})=>{
    return(
    <table>
        <th>
            First name
        </th>
        <th>
            Last_name
        </th>
        <th>
            Birthdate
        </th>
        {authors.map((author)=><AuthorItem author={author}/>)}
    </table>
    )
}

export default AuthorList;