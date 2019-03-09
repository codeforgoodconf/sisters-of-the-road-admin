import React, { Component } from 'react';


const AccountSummary = ({account, action}) => {
        return (
            <div id="account-summary" className="blue oswald ml4 pb4 fl w-40">
                <h1 className='f1'>{account.name}</h1>
                <p className="f2">
                    Current Balance:
                    <span className="gray"> ${account.balance}</span>
                </p>

                <p className="f3">Last Worked: {account.last_add}</p>
                <p className="f3">Last Purchase: {account.last_subtract}</p>

                <button className="f4 ph3 pv2 mb2 mr3 dib h3 w-50 white bg-blue"
                    onClick={action}>
                        <i className="fas fa-angle-double-left pr2"></i>
                        Back to Search
                </button>
            </div>
         );
    
}

export default AccountSummary;
