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
        return (
            <div className="SearchPage">
                <header>
                    <h1 class="text-center">Sisters of the Road Cafe</h1>
                </header>
                <div id="seachbar">
                    <input className="input-lg center-block" typeName="text" placeholder="Search for patron"/>
                </div>
                <div className="row">
                {accounts.map((account) =>
                    <div id="result" className="jumbotron row text-center center-block"
                         onClick={() => this.props.switchView('accountpage', account)}
                         key={account.id}>
                        <p>
                            {account.name}
                            <span>Last credit: {account.lastCredit}</span>
                            <span>Last meal: {account.lastMeal}</span>
                        </p>
                    </div>
                )}
                </div>
            </div>
         );
    }
}

export default SearchPage;
