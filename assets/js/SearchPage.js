import React, { Component } from 'react';


class SearchPage extends Component {
    constructor () {
        super();
    }

    render () {
         return (
            <div className="SearchPage">
                I'm the search page!
                <button onClick={() => this.props.switchView('accountpage')}>
                    John Doe
                </button>
            </div>
         );
    }
}

export default SearchPage;
