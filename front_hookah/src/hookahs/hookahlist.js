import React, { Component } from "react";
import HookahDetail from './hookahdetail';
import axios from 'axios'

class HookahList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            hookahsData : [],
            hookah: " ",
            showComponent: false,
        };
        this.getHookahDetail = this.getHookahDetail.bind(this);
        this.showHookahDetail = this.showHookahDetail.bind(this)
    }

    getHookahDetail(item) {
        axios.get("http://127.0.0.1:8000".concat(item.absolute_url))
                .then((response) => {
                    this.setState({hookah: response.data})
                    console.log()
                })
                .catch(function (error) {
                    console.log(error);
                });
    }


    showHookahDetail(item) {
        this.getHookahDetail(item);
        this.setState({ showComponent: true });
    }


    componentDidMount(){
        axios.get("http://127.0.0.1:8000")
        .then((response) => {
            this.setState({hookahsData: response.data})
        })
        .catch(function (error) {
            console.log(error);
        });
    }

    render(){
        return(
            <div>
                {
                    this.state.hookahsData.map(
                        (item) => {
                            return ( <h3 key={item.id} onClick = {
                                () => this.showHookahDetail(item)}>
                                {console.log(item)}
                                {item.hookah_name}, {item.city.name}, {item.street}</h3>
                            );
                        }
                    )
                }
                
                {this.state.showComponent ? (
                    <HookahDetail hookahDetail = {this.state.hookah} />
                ) : null}

            </div>
        )
    }
}

export default HookahList;