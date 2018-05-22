$(document).ready(()=>{
    //#region getData



    //#region  introduction scroll to
    let servicesSection = $('.services-section');

    $('.introduction-section__move-to-next').on('click', ()=> {
        let servicesSectionPosition = servicesSection.position().top;
        disableScroll()
        
        $('html, body').animate({
            scrollTop: servicesSectionPosition
        }, 700, enableScroll);

    });
    //#endregion

    //#region works tabs
    let tabItems    = $('.works-section__nav-list-item');
    let tabItemLine = $('.works-section__current-nav-item-line');

    tabItems.on('click', (e)=> {
        let tab         = $(e.currentTarget);
        let dataType    = tab.attr('data-type');
        let workItems   = $('.works-section__item');
        
        showResultByFilter(dataType, workItems);
        moveTabLine(tab);
    });

    function showResultByFilter(dataType, items) {
        items.each((index, item)=>{
                item        = $(item);
            let itemType    = item.attr('data-type');
            
            
            if(dataType === 'all') {
                item.css('display', 'block')

                item.animate({
                    "opacity": 1
                })
            }
            else if(itemType === dataType) {
                item.animate({
                    "opacity": 1
                }, ()=> {
                    item.css('display', 'block')
                })
            }
            else if(itemType !== dataType) {
                item.animate({
                    "opacity": 0
                }, ()=> {
                    item.css('display', 'none');
                })
            }
        });
    }

    function moveTabLine(tab) {
        let offset = tab.offset().left - $('.works-section__nav-list-item[data-tab-index="1"]').offset().left;

        tabItemLine.animate({
            'width': tab.width(),
            'margin-left': offset
        }, 400)
    }

    //#endregion
    
});

//#region helpers
function preventDefault(e) {
    e = e || window.event;
    if (e.preventDefault)
        e.preventDefault();
    e.returnValue = false;  
}
  
function preventDefaultForScrollKeys(e) {
    if (keys[e.keyCode]) {
        preventDefault(e);
        return false;
    }
}
  
function disableScroll() {
    if (window.addEventListener) // older FF
        window.addEventListener('DOMMouseScroll', preventDefault, false);
    window.onwheel = preventDefault; // modern standard
    window.onmousewheel = document.onmousewheel = preventDefault; // older browsers, IE
    window.ontouchmove  = preventDefault; // mobile
    document.onkeydown  = preventDefaultForScrollKeys;
}
  
function enableScroll() {
    if (window.removeEventListener)
        window.removeEventListener('DOMMouseScroll', preventDefault, false);
    window.onmousewheel = document.onmousewheel = null; 
    window.onwheel = null; 
    window.ontouchmove = null;  
    document.onkeydown = null;  
}

//#endregion