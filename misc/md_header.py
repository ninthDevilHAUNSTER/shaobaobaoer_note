from datetime import datetime


def gen(md_ed_type="", title='', author='shaobaobaoer', mail='shaobaobaoer@126.com', website='shaobaobaoer.cn',
        st_id='xxxx'):
    '''
    USAGE
        目前支持cmdmarkdown 和 typra 的头部生成
        主要参数为 md_ed_type 可以写为 'cmd' 或者 'ty'
        你们若是想要用的话，可以把一些默认的东西改一改
    :param md_ed_type:
    :param title:
    :param author:
    :param mail:
    :param website:
    :param st_id:
    :return:
    '''
    if md_ed_type == 'cmdmarkdown' or md_ed_type == 'cmd':
        print('''
>  \************************************************************************
	\> File Name: {title}
	\> Author: {name}
	\> Student-Id: {st_id}
	\> Mail: {mail}
	\> WebSite: {website}
	\> Time: {edtime}
 \************************************************************************
        '''.format(edtime=datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
                   , title=title, name=author, st_id=st_id, website=website, mail=mail))

    elif md_ed_type == 'typora' or md_ed_type == 'ty':
        print('''
>  \*******************************************************************************************************************************************
>
>  \> File Name: {title}
>
>  \>  Author: {name}
>
>  \>  Student-Id: {st_id}
>
>  \>  Mail: {mail}
>
>  \>  WebSite: {website}
>
>  \>  Time: {edtime}
>
>  \*******************************************************************************************************************************************
        '''.format(edtime=datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
                   , title=title, name=author, st_id=st_id, website=website, mail=mail))
    elif md_ed_type == 'sublime' or md_ed_type == 'subl' or md_ed_type == 'su':
        pass
