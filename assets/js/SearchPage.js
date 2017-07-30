import React, { Component } from 'react';


class SearchPage extends Component {
    constructor () {
        super();
    }

    render () {
        const {
            accounts
        } = this.props;
        return (
            <div className="SearchPage">
                <header>
                    <h1 className="text-center">Sisters of the Road Cafe</h1>
                </header>
                <div id="seachbar">
                    <input className="input-lg center-block" type="text" placeholder="Search for patron"/>
                </div>
                <div className="row">
                {accounts.map((account) =>
                    <div id="result" className="jumbotron row text-center center-block"
                         onClick={() => this.props.switchView('accountpage', account)}
                         key={account.id}>
                        <p>
                            {account.name}
                            <span>Last credit: {account.lastCredit}</span>
                            <span>Last purchase: {account.lastMeal}</span>
                        </p>
                    </div>
                )}
                </div>
            </div>
         );
    }
}

export default SearchPage;
