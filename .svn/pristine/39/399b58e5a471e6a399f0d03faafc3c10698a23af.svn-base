#coding=utf-8




def get_html(stream,startTime, success_count, failure_count, error_count):
        """
        :param startTime: 开始时间
        :param duration: 运行时长
        :param status: 状态
        :param success_count: 通过数量
        :param failure_count: 失败数量
        :param error_count：错误数量
        :return:
        """

        """
        1.为了兼容邮件的样式，单独写一个报告，使用.format方式将拿到的用例执行结果动态赋值到表格中
       """

        template = '''
        <h1 style="color:green;">quark—UFO自动化测试报告</h1>
        开始时间:{startTime}<br/>
        <p style="color:blue;">结果概览 </p>
              <h2>详细数据，烦请点击查看附件</h2>
              <div align=center>
        <table border=1 cellspacing=0 cellpadding=0 style='border-collapse:collapse;border:none'>
            <tr>
                <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;background:#DBDBDB;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>用例总数</span><span lang=EN-US><o:p></o:p></span></p>
                    </td>
                <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;background:#DBDBDB;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>通过数量</span><span lang=EN-US><o:p></o:p></span></p>
                    </td>
                 <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;background:#DBDBDB;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>失败数量</span><span lang=EN-US><o:p></o:p></span></p>
                </td>
                <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;background:#DBDBDB;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>错误数量</span><span lang=EN-US><o:p></o:p></span></p>
                    </td>
            </tr>

            <tr>
               <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>{full_success}</span><span lang=EN-US><o:p></o:p></span></p>
                    </td>
                <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>{success_count}</span><span lang=EN-US><o:p></o:p></span></p>
                    </td>
                 <td  bgcolor="red"   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0p;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>{failure_count}</span><span lang=EN-US><o:p></o:p></span></p>
                </td>
                <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;background:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>{error_count}</span><span lang=EN-US><o:p></o:p></span></p>
                    </td>
            </tr>
        </table>
        </div>
        '''.format(startTime=startTime,
                   full_success=success_count + failure_count + error_count, success_count=success_count,
                   failure_count=failure_count, error_count=error_count)
        stream.write(template)




