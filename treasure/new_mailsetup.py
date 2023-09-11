# from flask import Flask, jsonify, request
import smtplib  # Import smtplib for the actual sending function
from email.message import EmailMessage  # Import the email modules we'll need
from flask import Flask, request, url_for
import codecs


themoe_gmail_app_password = 'tfhuqepamclgetua'
themoe_gmail_id = 'support@themoe.com'


def email_send(email, choice, otp_code):
    # email = request.form.get('email')
    # SMTP stuff
    print('sending mail to', email)
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    print('sending...')
    s.starttls()
    s.login(themoe_gmail_id, themoe_gmail_app_password)
    print('sending...after login....')

    # Email Notifications for each actions
    msg = EmailMessage()

    # Email Verification for first time user
    if choice == 1:
        print(' in choice 1')
        msg['Subject'] = 'OTP confirmation!'
        # link = url_for('auth.confirm_email', token=token, _external=True)
        otp = otp_code
        msg.set_content(
            f"""\
			<!DOCTYPE html>
			<html>
   
   
			<body>
            <div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">
            <div style="margin:50px auto;width:70%;padding:20px 0">
                <div style="border-bottom:1px solid #eee">
                <a href="" style="font-size:1.4em;color: #00466a;text-decoration:none;font-weight:600">TheMoe</a>
                </div>
                <p style="font-size:1.1em">Hi,</p>
                <p>Use the following OTP to continue your password changing procedure. OTP is valid for 5 minutes</p>
                <h2 style="background: #00466a;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">{otp}</h2>
                <p style="font-size:0.9em;">Regards,<br />The Moe Team</p>
                <hr style="border:none;border-top:1px solid #eee" />
                <div style="float:right;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300">
                </div>
            </div>
            </div>
			</body>
            </html>""", subtype='html')
        print('email sent successfully')
    # Account activated after verifying email
    elif choice == 2:
        print(' in account confirmation')
        msg['Subject'] = 'Account Confirmation'
        msg.set_content(f'Hey! {email} is activated.')
    # Mail notification send to Host regarding new session
    elif choice == 3:
        print(' in new session creation')
        msg['Subject'] = 'New session Created!'
        msg.set_content(
            f'This host {email} has created a session sucessfully.')
    # Password updated Mail notification
    elif choice == 9:
        print('in password updation')
        msg['Subject'] = 'Password updated!'
        msg.set_content(f""" 
            <!DOCTYPE html
                PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html
                style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;">

            <head>
                <meta charset="UTF-8">
                <meta content="width=device-width, initial-scale=1" name="viewport">
                <meta name="x-apple-disable-message-reformatting">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta content="telephone=no" name="format-detection">
                <title>Thank you</title>
                <!--[if (mso 16)]><style type="text/css">     a {{text-decoration: none;}}     </style><![endif]-->
                <!--[if gte mso 9]><style>sup {{ font-size: 100% !important; }}</style><![endif]-->
                <style type="text/css">
                    @media only screen and (max-width:600px) {{

                        p,
                        ul li,
                        ol li,
                        a {{
                            font-size: 16px !important;
                            line-height: 150% !important
                        }}

                        h1 {{
                            font-size: 30px !important;
                            text-align: center;
                            line-height: 120% !important
                        }}

                        h2 {{
                            font-size: 26px !important;
                            text-align: center;
                            line-height: 120% !important
                        }}

                        h3 {{
                            font-size: 20px !important;
                            text-align: center;
                            line-height: 120% !important
                        }}

                        h1 a {{
                            font-size: 30px !important
                        }}

                        h2 a {{
                            font-size: 26px !important
                        }}

                        h3 a {{
                            font-size: 20px !important
                        }}

                        .es-menu td a {{
                            font-size: 14px !important
                        }}

                        .es-header-body p,
                        .es-header-body ul li,
                        .es-header-body ol li,
                        .es-header-body a {{
                            font-size: 14px !important
                        }}

                        .es-footer-body p,
                        .es-footer-body ul li,
                        .es-footer-body ol li,
                        .es-footer-body a {{
                            font-size: 14px !important
                        }}

                        .es-infoblock p,
                        .es-infoblock ul li,
                        .es-infoblock ol li,
                        .es-infoblock a {{
                            font-size: 12px !important
                        }}

                        *[class="gmail-fix"] {{
                            display: none !important
                        }}

                        .es-m-txt-c,
                        .es-m-txt-c h1,
                        .es-m-txt-c h2,
                        .es-m-txt-c h3 {{
                            text-align: center !important
                        }}

                        .es-m-txt-r,
                        .es-m-txt-r h1,
                        .es-m-txt-r h2,
                        .es-m-txt-r h3 {{
                            text-align: right !important
                        }}

                        .es-m-txt-l,
                        .es-m-txt-l h1,
                        .es-m-txt-l h2,
                        .es-m-txt-l h3 {{
                            text-align: left !important
                        }}

                        .es-m-txt-r img,
                        .es-m-txt-c img,
                        .es-m-txt-l img {{
                            display: inline !important
                        }}

                        .es-button-border {{
                            display: block !important
                        }}

                        a.es-button {{
                            font-size: 20px !important;
                            display: block !important;
                            border-left-width: 0px !important;
                            border-right-width: 0px !important
                        }}

                        .es-btn-fw {{
                            border-width: 10px 0px !important;
                            text-align: center !important
                        }}

                        .es-adaptive table,
                        .es-btn-fw,
                        .es-btn-fw-brdr,
                        .es-left,
                        .es-right {{
                            width: 100% !important
                        }}

                        .es-content table,
                        .es-header table,
                        .es-footer table,
                        .es-content,
                        .es-footer,
                        .es-header {{
                            width: 100% !important;
                            max-width: 600px !important
                        }}

                        .es-adapt-td {{
                            display: block !important;
                            width: 100% !important
                        }}

                        .adapt-img {{
                            width: 100% !important;
                            height: auto !important
                        }}

                        .es-m-p0 {{
                            padding: 0px !important
                        }}

                        .es-m-p0r {{
                            padding-right: 0px !important
                        }}

                        .es-m-p0l {{
                            padding-left: 0px !important
                        }}

                        .es-m-p0t {{
                            padding-top: 0px !important
                        }}

                        .es-m-p0b {{
                            padding-bottom: 0 !important
                        }}

                        .es-m-p20b {{
                            padding-bottom: 20px !important
                        }}

                        .es-mobile-hidden,
                        .es-hidden {{
                            display: none !important
                        }}

                        .es-desk-hidden {{
                            display: table-row !important;
                            width: auto !important;
                            overflow: visible !important;
                            float: none !important;
                            max-height: inherit !important;
                            line-height: inherit !important
                        }}

                        .es-desk-menu-hidden {{
                            display: table-cell !important
                        }}

                        table.es-table-not-adapt,
                        .esd-block-html table {{
                            width: auto !important
                        }}

                        table.es-social {{
                            display: inline-block !important
                        }}

                        table.es-social td {{
                            display: inline-block !important
                        }}
                    }}

                    #outlook a {{
                        padding: 0;
                    }}

                    .ExternalClass {{
                        width: 100%;
                    }}

                    .ExternalClass,
                    .ExternalClass p,
                    .ExternalClass span,
                    .ExternalClass font,
                    .ExternalClass td,
                    .ExternalClass div {{
                        line-height: 100%;
                    }}

                    .es-button {{
                        mso-style-priority: 100 !important;
                        text-decoration: none !important;
                    }}

                    a[x-apple-data-detectors] {{
                        color: inherit !important;
                        text-decoration: none !important;
                        font-size: inherit !important;
                        font-family: inherit !important;
                        font-weight: inherit !important;
                        line-height: inherit !important;
                    }}

                    .es-desk-hidden {{
                        display: none;
                        float: left;
                        overflow: hidden;
                        width: 0;
                        max-height: 0;
                        line-height: 0;
                        mso-hide: all;
                    }}
                </style>
            </head>

            <body
                style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;">
                <div class="es-wrapper-color" style="background-color:#F6F6F6;">
                    <!--[if gte mso 9]><v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t"> <v:fill type="tile" color="#f6f6f6"></v:fill> </v:background><![endif]-->
                    <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0"
                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;">
                        <tr style="border-collapse:collapse;">
                            <td valign="top" style="padding:0;Margin:0;">
                                <table cellpadding="0" cellspacing="0" class="es-content" align="center"
                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
                                    <tr style="border-collapse:collapse;">
                                        <td class="es-adaptive" align="center" style="padding:0;Margin:0;">
                                            <table class="es-content-body"
                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;"
                                                width="600" cellspacing="0" cellpadding="0" align="center">
                                                <tr style="border-collapse:collapse;">
                                                    <td align="left" style="padding:10px;Margin:0;">
                                                        <!--[if mso]><table width="580" cellpadding="0" cellspacing="0"><tr><td width="369" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left"
                                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tr style="border-collapse:collapse;">
                                                                <td class="es-m-p0r es-m-p20b" width="369" valign="top"
                                                                    align="center" style="padding:0;Margin:0;">
                                                                    <table width="100%" cellspacing="0" cellpadding="0"
                                                                        role="presentation"
                                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                        
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="191" valign="top"><![endif]-->
                                                        <table cellspacing="0" cellpadding="0" align="right"
                                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tr style="border-collapse:collapse;">
                                                                <td width="191" align="left" style="padding:0;Margin:0;">
                                                                    <table width="100%" cellspacing="0" cellpadding="0"
                                                                        role="presentation"
                                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                        <tr style="border-collapse:collapse;">
                                                                            <td esdev-links-color="#999999" align="right"
                                                                                class="es-infoblock es-m-txt-c"
                                                                                style="padding:0;Margin:0;line-height:14px;font-size:12px;color:#999999;">
                                                                            
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                                <table cellpadding="0" cellspacing="0" class="es-header" align="center"
                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top;">
                                    <tr style="border-collapse:collapse;">
                                        <td class="es-adaptive" align="center" style="padding:0;Margin:0;">
                                            <table class="es-header-body" width="600" cellspacing="0" cellpadding="0" align="center"
                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;">
                                                <tr style="border-collapse:collapse;">
                                                    <td align="left" style="padding:0;Margin:0;padding-top:5px;padding-bottom:5px;">
                                                        <!--[if mso]><table width="600" cellpadding="0" cellspacing="0"><tr><td width="184" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left"
                                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tr style="border-collapse:collapse;">
                                                                <td class="es-m-p0r" width="184" valign="top" align="center"
                                                                    style="padding:0;Margin:0;">
                                                                    <table width="100%" cellspacing="0" cellpadding="0"
                                                                        role="presentation"
                                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                        <tr style="border-collapse:collapse;">
                                                                            <td class="es-m-p0l" align="center"
                                                                                style="padding:0;Margin:0;padding-top:10px;padding-bottom:10px;font-size:0;">
                                                                                <a href="https://xrconnect.io/" target=""
                                                                                    style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;text-decoration:underline;color:#999999;">
                                                                                    <img src="http://cdn.mcauto-images-production.sendgrid.net/88d00175aea446c9/9084e5be-331f-470e-af56-358c7fbe073b/2488x529.png"
                                                                                        alt="XR Connect logo"
                                                                                        title="XR Connect logo" width="178"
                                                                                        height="41"
                                                                                        style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;"></a>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                        <!--[if mso]></td><td width="33"></td><td width="383" valign="top"><![endif]-->
                                                        <table cellspacing="0" cellpadding="0" align="right"
                                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tr style="border-collapse:collapse;">
                                                                <td width="383" align="left" style="padding:0;Margin:0;">
                                                                    <table width="100%" cellspacing="0" cellpadding="0"
                                                                        role="presentation"
                                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                        <tr style="border-collapse:collapse;">
                                                                            <td style="padding:0;Margin:0;">
                                                                                <table class="es-menu" width="100%" cellspacing="0"
                                                                                    cellpadding="0" role="presentation"
                                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                                    <tr class="links"
                                                                                        style="border-collapse:collapse;">
                                                                                        <td style="Margin:0;padding-left:5px;padding-right:5px;padding-top:23px;padding-bottom:5px;border:0;"
                                                                                            width="33.33%" bgcolor="transparent"
                                                                                            align="center"><a target="_blank"
                                                                                                style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;text-decoration:none;display:block;color:#666666;"
                                                                                                href="tel:123456789">+91 90009-25709</a>
                                                                                        </td>
                                                                                        <td style="Margin:0;padding-left:5px;padding-right:5px;padding-top:23px;padding-bottom:5px;border:0;"
                                                                                            width="33.33%" bgcolor="transparent"
                                                                                            align="center">
                                                                                            <a target="_blank"
                                                                                                style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;text-decoration:none;display:block;color:#666666;"
                                                                                                href="mailto:support@xrconnect.io">support@xrconnect.io</a>
                                                                                        </td>
                                                                                        <!-- <td class="es-hidden"
                                                                                            style="Margin:0;padding-left:5px;padding-right:5px;padding-top:23px;padding-bottom:5px;border:0;"
                                                                                            width="33.33%" bgcolor="transparent"
                                                                                            align="center"><a target="_blank"
                                                                                                style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;text-decoration:none;display:block;color:#666666;"
                                                                                                href="">Online
                                                                                                Chat</a></td> -->
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr style="border-collapse:collapse;">
                                                    <td style="padding:5px;Margin:0px;" bgcolor="ff7069"
                                                        align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0"
                                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tr style="border-collapse:collapse;">
                                                                <td width="590" valign="top" align="center"
                                                                    style="padding:0;Margin:0;">
                                                                    <table width="100%" cellspacing="0" cellpadding="0"
                                                                        role="presentation"
                                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                        <tr style="border-collapse:collapse;">
                                                                            <td style="padding:0;Margin:0;">
                                                                                <table class="es-menu" width="100%" cellspacing="0"
                                                                                    cellpadding="0" role="presentation"
                                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                                    <tr class="links"
                                                                                        style="border-collapse:collapse;">
                                                                                        <td style="Margin:0;padding-left:5px;padding-right:5px;padding-top:8px;padding-bottom:8px;border:0;"
                                                                                            width="25.00%" bgcolor="transparent"
                                                                                            align="center"><p
                                                                                                style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:16px;text-decoration:none;display:block;color:#ffffff;">
                                                                                                <b>CONNECT . COMMUNICATE . COLLABORATE</b></p>
                                                                                        </td>
                                                                                    
                                                                                        
                                                                                        
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                                <table class="es-content" cellspacing="0" cellpadding="0" align="center"
                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
                                    <tr style="border-collapse:collapse;">
                                        <td align="center" style="padding:0;Margin:0;">
                                            <table class="es-content-body" width="600" cellspacing="0" cellpadding="0"
                                                bgcolor="#ffffff" align="center"
                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;">
                                                <tr style="border-collapse:collapse;">
                                                    <td align="left" style="padding:0;Margin:0;">
                                                        <table width="100%" cellspacing="0" cellpadding="0"
                                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tr style="border-collapse:collapse;">
                                                                <td width="600" valign="top" align="center"
                                                                    style="padding:0;Margin:0;">
                                                                    <table width="100%" cellspacing="0" cellpadding="0"
                                                                        role="presentation"
                                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                        <tr style="border-collapse:collapse;">
                                                                            <td style="padding:0;Margin:0;position:relative;"
                                                                                align="center"><a target="_blank"
                                                                                    href=""
                                                                                    style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;text-decoration:underline;color:#FAA41D;"><img
                                                                                        class="adapt-img"
                                                                                        src="http://cdn.mcauto-images-production.sendgrid.net/88d00175aea446c9/c8bb20f4-a02b-4855-ab99-a1fd5d9fad1b/700x300.png"
                                                                                        alt=""
                                                                                        title=""
                                                                                        width="600" height="auto"
                                                                                        style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;"></a>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                                <table class="es-content" cellspacing="0" cellpadding="0" align="center"
                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
                                    <tr style="border-collapse:collapse;">
                                        <td align="center" style="padding:0;Margin:0;">
                                            <table class="es-content-body" width="600" cellspacing="0" cellpadding="0"
                                                bgcolor="#ffffff" align="center"
                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;">
                                                <tr style="border-collapse:collapse;">
                                                    <td align="left"
                                                        style="padding:0;Margin:0;padding-top:20px;padding-left:20px;padding-right:20px;">
                                                        <table width="100%" cellspacing="0" cellpadding="0"
                                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tr style="border-collapse:collapse;">
                                                                <td width="560" valign="top" align="center"
                                                                    style="padding:0;Margin:0;">
                                                                    <table
                                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:separate;border-spacing:0px;border-width:0px 0px 2px;border-style:solid;border-color:#FFFFFF #FFFFFF #f85a61;"
                                                                        width="100%" cellspacing="0" cellpadding="0"
                                                                        role="presentation">
                                                                        
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr style="border-collapse:collapse;">
                                                    <table width="100%" cellspacing="0" cellpadding="0"
                                                    role="presentation"
                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                    
                                                    <!-- <tr style="border-collapse:collapse;">
                                                        <td align="center" style="padding:40px;Margin:0px auto!important;"><span
                                                                class="es-button-border"
                                                                style="border-style:solid;border-color:#f85a61;background:#f85a61 none repeat scroll 0% 0%;border-width:0px;display:inline-block;border-radius:0px;width:auto;">
                                                                <a href="https://xrconnect.io"
                                                                    class="es-button" target="_blank"
                                                                    style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:18px;color:#EFEFEF;border-style:solid;border-color:#f85a61;border-width:10px 20px 10px 20px;display:inline-block;background:#f85a61 none repeat scroll 0% 0%;border-radius:0px;font-weight:normal;font-style:normal;line-height:22px;width:auto;text-align:center;border-radius: 100px;">Verify</a></span></td>
                                                    </tr> -->
                                                    <tr style="border-collapse:collapse;">
                                                        <td align="center"
                                                            style="padding:20px;Margin:0;padding-bottom:25px;">
                                                            <p
                                                                style="Margin:0;line-height:29px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:24px;font-style:normal;font-weight:normal;color:#333333;">
                                                                Dear<span
                                                                style="line-height:120%; font-weight: 700;"> User,</span> <br>Your password has been succeessfully updated.</p>
                                                        </td>
                                                    </tr>
                                                </table>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                                
                                <table cellpadding="0" cellspacing="0" class="es-footer" align="center"
                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top;">
                                    <tr style="border-collapse:collapse;">
                                        <td align="center" style="padding:0;Margin:0;">
                                            <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" align="center"
                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#EFEFEF;">
                                                <tr style="border-collapse:collapse;">
                                                    <td align="left" style="padding:20px;Margin:0;">
                                                        <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="356" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left"
                                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tr style="border-collapse:collapse;">
                                                                <td class="es-m-p20b" width="356" align="left"
                                                                    style="padding:0;Margin:0;">
                                                                    <table width="100%" cellspacing="0" cellpadding="0"
                                                                        role="presentation"
                                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                        <tr style="border-collapse:collapse;">
                                                                            <td esdev-links-color="#666666" align="left"
                                                                                style="padding:0;Margin:0;">
                                                                                <p
                                                                                    style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:28px;color:#666666;">
                                                                                    © 2021 Reinvision. All rights reserved.</p>
                                                                                <p
                                                                                    style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:28px;color:#666666;">
                                                                                    You're receiving this email because you
                                                                                    subscribed our site.</p>
                                                                                <p
                                                                                    style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:28px;color:#666666;">
                                                                                    <a target="_blank" class="unsubscribe" href=""
                                                                                        style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;text-decoration:underline;color:#666666;">Unsubscribe</a>
                                                                                </p>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="184" valign="top"><![endif]-->
                                                        <table cellspacing="0" cellpadding="0" align="right"
                                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tr style="border-collapse:collapse;">
                                                                <td width="184" align="left" style="padding:0;Margin:0;">
                                                                    <table width="100%" cellspacing="0" cellpadding="0"
                                                                        role="presentation"
                                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                        <tr style="border-collapse:collapse;">
                                                                            <td esdev-links-color="#666666" align="left"
                                                                                style="padding:0;Margin:0;">
                                                                                <!-- <p
                                                                                    style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:28px;color:#666666;">
                                                                                    <a target="_blank"
                                                                                        href=""
                                                                                        style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;text-decoration:underline;color:#666666;">Questions?</a>
                                                                                </p> -->
                                                                                <p
                                                                                    style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:28px;color:#666666;">
                                                                                    <a target=""
                                                                                        href="mailto:varun@reinvision.com"
                                                                                        style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;text-decoration:underline;color:#666666;">Email
                                                                                        us</a></p>
                                                                                <p
                                                                                    style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:28px;color:#666666;">
                                                                                    <a target="_blank"
                                                                                        style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;text-decoration:underline;color:#666666;line-height:28px;"
                                                                                        href="tel:+91 90009-25709">+91 90009-25709</a></p>
                                                                            </td>
                                                                        </tr>
                                                                        <!-- <tr style="border-collapse:collapse;">
                                                                            <td align="left"
                                                                                style="padding:0;Margin:0;padding-top:5px;font-size:0;">
                                                                                <table class="es-table-not-adapt es-social"
                                                                                    cellspacing="0" cellpadding="0"
                                                                                    role="presentation"
                                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                                    <tr style="border-collapse:collapse;">
                                                                                        <td valign="top" align="center"
                                                                                            style="padding:0;Margin:0;padding-right:10px;">
                                                                                            <img title="Twitter"
                                                                                                src=""
                                                                                                alt="Tw" width="24" height="24"
                                                                                                style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;">
                                                                                        </td>
                                                                                        <td valign="top" align="center"
                                                                                            style="padding:0;Margin:0;padding-right:10px;">
                                                                                            <img title="Facebook"
                                                                                                src=""
                                                                                                alt="Fb" width="24" height="24"
                                                                                                style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;">
                                                                                        </td>
                                                                                        <td valign="top" align="center"
                                                                                            style="padding:0;Margin:0;padding-right:10px;">
                                                                                            <img title="Youtube"
                                                                                                src=""
                                                                                                alt="Yt" width="24" height="24"
                                                                                                style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;">
                                                                                        </td>
                                                                                        <td valign="top" align="center"
                                                                                            style="padding:0;Margin:0;"><img
                                                                                                title="Vkontakte"
                                                                                                src=""
                                                                                                alt="Vk" width="24" height="24"
                                                                                                style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;">
                                                                                        </td>
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                        </tr> -->
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                                <table class="es-content" cellspacing="0" cellpadding="0" align="center"
                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
                                    <tr style="border-collapse:collapse;">
                                        <td align="center" style="padding:0;Margin:0;">
                                            <table class="es-content-body"
                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;"
                                                width="600" cellspacing="0" cellpadding="0" align="center">
                                                <tr style="border-collapse:collapse;">
                                                    <td align="left"
                                                        style="Margin:0;padding-left:20px;padding-right:20px;padding-top:30px;padding-bottom:30px;">
                                                        <table width="100%" cellspacing="0" cellpadding="0"
                                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                            <tr style="border-collapse:collapse;">
                                                                <td width="560" valign="top" align="center"
                                                                    style="padding:0;Margin:0;">
                                                                    <table width="100%" cellspacing="0" cellpadding="0"
                                                                        role="presentation"
                                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                                                                        <tr style="border-collapse:collapse;">
                                                                            <td class="es-infoblock made_with" align="center"
                                                                                style="padding:0;Margin:0;line-height:120%;font-size:0;color:#999999;">
                                                                                <a target="_blank"
                                                                                    href=""
                                                                                    style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:12px;text-decoration:underline;color:#999999;"><img
                                                                                        src=""
                                                                                        alt width="auto" height="56"
                                                                                        style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;"></a>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </div>
            </body>

            </html>
                        
                        """, subtype='html')

    elif choice == 4:
        msg['Subject'] = 'Qualifed student'
        
        msg.set_content(
            f'This {email} has registered for treasure hunt sucessfully.')
    else:
        print(f'Please enter correct details')

    # the recipient's email address
    msg['From'] = 'TheMoe <support@themoe.com>'
    msg['To'] = f'{email}'  # the sender's email address
    # msg['Bcc'] = ['XR Connect<support@xrconnect.io>', 'siddharth@reinvision.com']
    s.send_message(msg)
    s.quit()
    return 'Email sent!'
