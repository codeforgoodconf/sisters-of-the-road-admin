import React, { Component } from 'react';


class SearchPage extends Component {
    constructor () {
        super();
        this.state = {
            accounts: [
                {
                    name: 'John Doe',
                    id: '1',
                    lastCredit: '7/20/17',
                    lastMeal: '5/30/17',
                    currentCredit: 4.25
                },
                {
                    name: 'Josey',
                    id: '2',
                    lastCredit: '7/20/17',
                    lastMeal: '5/30/17',
                    currentCredit: 1.75
                },
                {
                    name: 'J Odin',
                    id: '3',
                    lastCredit: '7/20/17',
                    lastMeal: '5/30/17',
                    currentCredit: 3.00
                },
            ]
        };
    }

    render () {
        const {
            accounts
        } = this.state;
        console.log(accounts);
        return (
            <div className="SearchPage">
                I'm the search page!

                {accounts.map((account) =>
                    <div style={{borderStyle: 'solid', margin: '5px'}}
                         onClick={() => this.props.switchView('accountpage', account)}
                         key={account.id}>
                        <p>{account.name}</p>
                        <p>Last credit: {account.lastCredit}</p>
                        <p>Last meal: {account.lastMeal}</p>
                    </div>
                )}
            </div>
         );
    }
}

export default SearchPage;
