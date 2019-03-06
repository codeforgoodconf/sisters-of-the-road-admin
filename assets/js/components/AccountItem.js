import React from 'react'

const AccountListItem = ({ account, action}) => {
    return(
        <li className="bg-light-gray pv2 pa3 mb3 b--solid br1 b--moon-gray flex items-center" onClick={action} >
                            <span class="flex-auto">
                                <p> {account.name} </p>
                                <p> {account.balance} </p>
                                <p>Last credit: {account.last_add}</p>
                                <p>Last purchase: {account.last_subtract}</p>
                            </span>
                            <span class="f1 silver">&rsaquo;</span>
        </li>
    )
}


export default AccountListItem;