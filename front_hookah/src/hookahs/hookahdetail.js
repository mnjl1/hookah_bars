import React, { Component } from 'react'

class HookahDetail extends Component{
   
    render(){
        const obj = this.props.hookahDetail;
        
        return(
            // TODO move style to css
            <div style = {{ color: "yellow", border: "1px solid yellow"  }}>
                <h4>{obj.hookah_name}</h4>
                <h5>
                        <p>{obj.city}</p>
                        {obj.street}
                        <p>{obj.hookah_style}</p>
                        <p>{obj.phone}</p>
                        Tobacco: 
                        <div>
                            
                        </div>
                        <p>{obj.description}</p>
                        <p>{obj.credit_card}</p>
                        <p>{obj.summer_terrace}</p>
                        <div>
                            {obj.hookah_tobacco ? obj.hookah_tobacco.map(
                                (t) => {
                                    return (
                                        <div>{t.hookah_tobacco}</div>
                                    )
                                }
                            ) : null}
                        </div>
                </h5>
            </div>
        )
    }
}

export default HookahDetail;