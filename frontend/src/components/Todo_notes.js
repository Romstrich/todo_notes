import React from "react";


const TodoItem = ({todo_note}) =>{

    return(
    <tr>
        <td>
            {todo_note.project}
        </td>
        <td>
            {todo_note.created_at}
        </td>
        <td>
            {todo_note.updated_at}
        </td>
        <td>
            {todo_note.created_user}
        </td>
        <td>
            {todo_note.active}
        </td>
        <td>
            {todo_note.note_text}
        </td>
    </tr>
    )
}

const TodoList = ({todo_notes})=>{
    return(
    <table>
        <th>
            project
        </th>
        <th>
            created_at
        </th>
        <th>
            updated_at
        </th>
        <th>
            created_user
        </th>
        <th>
            active
        </th>
        <th>
            note_text
        </th>

        {todo_notes.map((todo_note)=><TodoItem todo_note={todo_note}/>)}
    </table>
    )
}

export default TodoList;