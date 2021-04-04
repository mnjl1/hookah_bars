import React, { Component } from 'react'

class HookahDetail extends Component{
   
    render(){
        const obj = this.props.hookahDetail;
        
        return(
            // TODO move style to css
            <div style = {{ color: "yellow", border: "1px solid yellow"  }}>
                <h4>{obj.hookah_name}</h4>
                <h5>
                        <p>{obj.city ? obj.city.name : null }, {obj.street}</p>
                        <p>{obj.hookah_style}</p>
                        <p>{obj.phone}</p>
                        <p>{obj.description}</p>
                        <p>Credit card: {obj.credit_card ? 'Yes' : 'No'}</p>
                        <p>Summer terrace {obj.summer_terrace ? 'Yes' : 'No'}</p>
                        Hookah Style:
                        <div>
                            {obj.hookah_type ? obj.hookah_type.map(
                                (s) => {
                                    return (
                                        <div>{s.hookah_type}</div>
                                    )
                                }
                            ) : null}

                        </div>
                        Hookah Tobacco:
                        <div>
                            {obj.hookah_tobacco ? obj.hookah_tobacco.map(
                                (t) => {
                                    return (
                                        <div>{t.hookah_tobacco}</div>
                                    )
                                }
                            ) : null}
                        </div>
                        <div>
                        {/* TODO fix displaying images */}
                            {/* {obj.hookah_images ? obj.hookah_images.map(
                                (image) => {
                                    return (
                                        <div>
                                            {console.log(image.hookah_image)}
                                            <image src={image.hookah_image}/>
                                        </div>
                                    )
                                }
                            ) : null} */}
                        </div>
                </h5>
            </div>
        )
    }
}

export default HookahDetail;