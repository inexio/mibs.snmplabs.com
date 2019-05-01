#
# PySNMP MIB module XYLAN-AVL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-AVL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:44:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, TimeTicks, Bits, IpAddress, Gauge32, ModuleIdentity, Unsigned32, Counter64, Counter32, MibIdentifier, iso, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Bits", "IpAddress", "Gauge32", "ModuleIdentity", "Unsigned32", "Counter64", "Counter32", "MibIdentifier", "iso", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xylanAVLArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanAVLArch")
xylanAVLConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 15, 1))
xylanAVLloginbanner = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLloginbanner.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLloginbanner.setDescription('The Authentication login banner')
xylanAVLoptionprompt = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLoptionprompt.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLoptionprompt.setDescription('Radius/LDAP telnet authentication type prompt')
xylanAVLgroupprompt = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLgroupprompt.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLgroupprompt.setDescription('Radius/LDAP authentication group prompt')
xylanAVLuserprompt = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLuserprompt.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLuserprompt.setDescription('Radius/LDAP authentication username prompt')
xylanAVLpassprompt = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLpassprompt.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLpassprompt.setDescription('Radius/LDAP authentication password prompt')
xylanAVLchalprompt = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLchalprompt.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLchalprompt.setDescription('Radius/LDAP authentication challenge prompt')
xylanAVLsucceedmsg = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLsucceedmsg.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLsucceedmsg.setDescription('Radius/LDAP successful authentication attempt message')
xylanAVLfailmsg = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLfailmsg.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLfailmsg.setDescription('Radius/LDAP failed authentication attempt message')
xylanAVLauthmode = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("single-authority", 1), ("multiple-authority", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLauthmode.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLauthmode.setDescription('Radius/LDAP authentication group mode: 1 - single authority 2 - multiple authority')
xylanAVLtimeout = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLtimeout.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLtimeout.setDescription('Radius/LDAP authentication client session timeout in seconds')
xylanAVLlastuser = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanAVLlastuser.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLlastuser.setDescription('Radius/LDAP last user event information. This is useful in determining the last authentication attempt')
xylanAVLlastauthevent = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("success", 1), ("failure", 2), ("logout", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanAVLlastauthevent.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLlastauthevent.setDescription('Radius/LDAP last authorization event type. The following events are valid: 1 - Successful Login 2 - Failed Login Attempt 3 - Logout/Drop Note: The xylanAVLlastuser MIB entry is only valid on events 1 and 2. Logouts and drops do NOT utilize this entry.')
xylanAVLlastauthmac = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 18), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanAVLlastauthmac.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLlastauthmac.setDescription('The last MAC Address to make an authentication attempt.')
xylanAVLlastport = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanAVLlastport.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLlastport.setDescription('The last port number from which the authentication attempt originated.')
xylanAVLlastslot = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanAVLlastslot.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLlastslot.setDescription('The last slot number from which the authentication attempt originated.')
xylanAVLversion = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanAVLversion.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLversion.setDescription('The Authenticated VLAN II module version information.')
xylanAVLdropmac = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 22), MacAddress()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: xylanAVLdropmac.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLdropmac.setDescription('Drop the connection associated with this particular MAC address.')
xylanAVLradretries = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLradretries.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLradretries.setDescription('The number of retries sent to the Radius server before the request is timed out.')
xylanAVLradtimeout = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 24), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLradtimeout.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLradtimeout.setDescription('The number of seconds to wait before another request is sent to the Radius server.')
xylanAVLBootpIfAddr = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 25), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLBootpIfAddr.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLBootpIfAddr.setDescription('The IP address of the interface on the switch through which the DHCP requests are forwarded.')
xylanAVLDNSName = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 26), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLDNSName.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLDNSName.setDescription('The host name used to represent the authentication IP address configured on the switch.')
xylanAVLPathRestriction = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 27), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLPathRestriction.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLPathRestriction.setDescription('For security reasons it is necessary to limit a web based user to a particular directory. This is the path to which he is restricted . The Path must have the form /dir1name/dir2name/etc.')
xylanAVLTproxyports = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 2), )
if mibBuilder.loadTexts: xylanAVLTproxyports.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLTproxyports.setDescription('The Telnet Authentication proxy address list enumerates the list of IP addresses that the switch recognizes as authentication addresses.')
xylanAVLTproxyentry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 2, 1), ).setIndexNames((0, "XYLAN-AVL-MIB", "xylanAVLTproxyIntfAddr"))
if mibBuilder.loadTexts: xylanAVLTproxyentry.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLTproxyentry.setDescription('The Telnet Authentication proxy address')
xylanAVLTproxyIntfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 2, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLTproxyIntfAddr.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLTproxyIntfAddr.setDescription('This value gives the IP address of the router port to which the proxy address applies')
xylanAVLTproxyProxyAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLTproxyProxyAddr.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLTproxyProxyAddr.setDescription('This value gives the proxy IP address')
xylanAVLRadiusServers = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13), )
if mibBuilder.loadTexts: xylanAVLRadiusServers.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusServers.setDescription('Listing of Configured Radius Authentication Servers by group.')
xylanAVLradiusentry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1), ).setIndexNames((0, "XYLAN-AVL-MIB", "xylanAVLRadiusAddress"), (0, "XYLAN-AVL-MIB", "xylanAVLRadiusGroup"))
if mibBuilder.loadTexts: xylanAVLradiusentry.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLradiusentry.setDescription('Individual Radius Authentication Server Entry.')
xylanAVLRadiusGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLRadiusGroup.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusGroup.setDescription('The group number to which the Radius server is assigned.')
xylanAVLRadiusAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLRadiusAddress.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusAddress.setDescription('Radius Server IP address.')
xylanAVLRadiusPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLRadiusPriority.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusPriority.setDescription('The radius servers priority in the list of configured servers, 1 being the highest.')
xylanAVLRadiusPort = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLRadiusPort.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusPort.setDescription('The radius server remote UDP port number')
xylanAVLRadiusSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1, 5), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: xylanAVLRadiusSecret.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusSecret.setDescription('The radius servers secret.')
xylanAVLRadiusAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 13, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLRadiusAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusAdminState.setDescription('The current status of this server, active (1) or delete(2) to tell SNMP to delete this entry')
xylanAVLRadiusAcctServers = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14), )
if mibBuilder.loadTexts: xylanAVLRadiusAcctServers.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusAcctServers.setDescription('Listing of Configured Radius Authentication Servers by group.')
xylanAVLradiusacctentry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1), ).setIndexNames((0, "XYLAN-AVL-MIB", "xylanAVLRadiusAcctAddress"), (0, "XYLAN-AVL-MIB", "xylanAVLRadiusAcctGroup"))
if mibBuilder.loadTexts: xylanAVLradiusacctentry.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLradiusacctentry.setDescription('Individual Radius Authentication Server Entry.')
xylanAVLRadiusAcctGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLRadiusAcctGroup.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusAcctGroup.setDescription('The group number to which the Radius server is assigned.')
xylanAVLRadiusAcctAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLRadiusAcctAddress.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusAcctAddress.setDescription('Radius Server IP address.')
xylanAVLRadiusAcctPri = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLRadiusAcctPri.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusAcctPri.setDescription('The server priority in the list, one being the highest.')
xylanAVLRadiusAcctPort = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLRadiusAcctPort.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusAcctPort.setDescription('The radius server remote UDP port number')
xylanAVLRadiusAcctSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1, 5), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: xylanAVLRadiusAcctSecret.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusAcctSecret.setDescription('The radius servers secret.')
xylanAVLRadiusAcctAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 14, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLRadiusAcctAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLRadiusAcctAdminState.setDescription('The current status of this server, active (1) or delete(2) to tell SNMP to delete this entry')
class XylanAVLtelportStatCodes(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disable", 1), ("enable", 2))

xylanAVLtelports = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 3), )
if mibBuilder.loadTexts: xylanAVLtelports.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLtelports.setDescription('The Telnet Authentication enabled list enumerates the list of Telnet authentication enabled ports')
xylanAVLtelportentry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 3, 1), ).setIndexNames((0, "XYLAN-AVL-MIB", "xylanAVLtelportslot"), (0, "XYLAN-AVL-MIB", "xylanAVLtelportport"))
if mibBuilder.loadTexts: xylanAVLtelportentry.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLtelportentry.setDescription('The Telnet Authentication port description')
xylanAVLtelportslot = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLtelportslot.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLtelportslot.setDescription('This value gives the physical slot in the Switch')
xylanAVLtelportport = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLtelportport.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLtelportport.setDescription('This value gives the physical port within a slot in the Switch')
xylanAVLtelportstat = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 3, 1, 3), XylanAVLtelportStatCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLtelportstat.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLtelportstat.setDescription('This value gives status of the port. Used for deleting entries')
xylanAVLLdapServers = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28), )
if mibBuilder.loadTexts: xylanAVLLdapServers.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapServers.setDescription('Listing of LDAP Authentication Servers by group.')
xylanAVLLdapentry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1), ).setIndexNames((0, "XYLAN-AVL-MIB", "xylanAVLLdapGroup"))
if mibBuilder.loadTexts: xylanAVLLdapentry.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapentry.setDescription('Individual Authentication LDAP Server Entry')
xylanAVLLdapGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLLdapGroup.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapGroup.setDescription('The group number to which the LDAP server is assigned.')
xylanAVLLdapUserId = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLLdapUserId.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapUserId.setDescription('LDAP server super user id.')
xylanAVLLdapUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 3), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: xylanAVLLdapUserPassword.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapUserPassword.setDescription('LDAP server super user password.')
xylanAVLLdapSearchBase = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLLdapSearchBase.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapSearchBase.setDescription('LDAP server search base.')
xylanAVLLdapChain = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLLdapChain.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapChain.setDescription('LDAP server chain.')
xylanAVLLdapType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("generic-schema", 1), ("netscape-directory-server", 2), ("novell-NDS", 3), ("sun-directory-services", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLLdapType.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapType.setDescription('LDAP server type. 1 - Generic Schema 2 - Netscape Directory Server 3 - Novell NDS 4 - Sun Directory Services')
xylanAVLLdapRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLLdapRetry.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapRetry.setDescription('LDAP server retry times.')
xylanAVLLdapResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 90))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLLdapResponseTime.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapResponseTime.setDescription('LDAP server response time in seconds.')
xylanAVLLdapAcctStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLLdapAcctStatus.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapAcctStatus.setDescription('LDAP accounting status: 1 - on 2 - off')
xylanAVLLdapLoginFailId = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLLdapLoginFailId.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapLoginFailId.setDescription('LDAP server login fail id.')
xylanAVLLdapMultiGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLLdapMultiGroup.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapMultiGroup.setDescription('LDAP multiple mode has group data: 1 - yes 2 - no')
xylanAVLLdapAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 15, 1, 28, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanAVLLdapAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: xylanAVLLdapAdminState.setDescription('The current status of this server: active (1): Server chain is active. delete (2): tell SNMP to delete this entry.')
mibBuilder.exportSymbols("XYLAN-AVL-MIB", xylanAVLradretries=xylanAVLradretries, xylanAVLRadiusServers=xylanAVLRadiusServers, xylanAVLRadiusAcctAdminState=xylanAVLRadiusAcctAdminState, xylanAVLtelports=xylanAVLtelports, xylanAVLoptionprompt=xylanAVLoptionprompt, xylanAVLchalprompt=xylanAVLchalprompt, xylanAVLRadiusAcctGroup=xylanAVLRadiusAcctGroup, xylanAVLLdapChain=xylanAVLLdapChain, xylanAVLuserprompt=xylanAVLuserprompt, xylanAVLradtimeout=xylanAVLradtimeout, xylanAVLLdapServers=xylanAVLLdapServers, xylanAVLLdapUserPassword=xylanAVLLdapUserPassword, xylanAVLLdapType=xylanAVLLdapType, xylanAVLloginbanner=xylanAVLloginbanner, xylanAVLversion=xylanAVLversion, xylanAVLLdapRetry=xylanAVLLdapRetry, xylanAVLlastauthmac=xylanAVLlastauthmac, xylanAVLlastslot=xylanAVLlastslot, xylanAVLlastauthevent=xylanAVLlastauthevent, xylanAVLradiusentry=xylanAVLradiusentry, xylanAVLRadiusPriority=xylanAVLRadiusPriority, xylanAVLRadiusAcctServers=xylanAVLRadiusAcctServers, xylanAVLLdapResponseTime=xylanAVLLdapResponseTime, XylanAVLtelportStatCodes=XylanAVLtelportStatCodes, xylanAVLRadiusAcctAddress=xylanAVLRadiusAcctAddress, xylanAVLlastport=xylanAVLlastport, xylanAVLDNSName=xylanAVLDNSName, xylanAVLTproxyports=xylanAVLTproxyports, xylanAVLsucceedmsg=xylanAVLsucceedmsg, xylanAVLPathRestriction=xylanAVLPathRestriction, xylanAVLRadiusPort=xylanAVLRadiusPort, xylanAVLtelportentry=xylanAVLtelportentry, xylanAVLLdapGroup=xylanAVLLdapGroup, xylanAVLLdapentry=xylanAVLLdapentry, xylanAVLLdapAcctStatus=xylanAVLLdapAcctStatus, xylanAVLTproxyProxyAddr=xylanAVLTproxyProxyAddr, xylanAVLtelportstat=xylanAVLtelportstat, xylanAVLRadiusGroup=xylanAVLRadiusGroup, xylanAVLradiusacctentry=xylanAVLradiusacctentry, xylanAVLtelportslot=xylanAVLtelportslot, xylanAVLgroupprompt=xylanAVLgroupprompt, xylanAVLLdapAdminState=xylanAVLLdapAdminState, xylanAVLfailmsg=xylanAVLfailmsg, xylanAVLdropmac=xylanAVLdropmac, xylanAVLTproxyentry=xylanAVLTproxyentry, xylanAVLlastuser=xylanAVLlastuser, xylanAVLRadiusSecret=xylanAVLRadiusSecret, xylanAVLRadiusAcctPri=xylanAVLRadiusAcctPri, xylanAVLLdapMultiGroup=xylanAVLLdapMultiGroup, xylanAVLLdapUserId=xylanAVLLdapUserId, xylanAVLtelportport=xylanAVLtelportport, xylanAVLBootpIfAddr=xylanAVLBootpIfAddr, xylanAVLtimeout=xylanAVLtimeout, xylanAVLTproxyIntfAddr=xylanAVLTproxyIntfAddr, xylanAVLConfig=xylanAVLConfig, xylanAVLLdapSearchBase=xylanAVLLdapSearchBase, xylanAVLRadiusAdminState=xylanAVLRadiusAdminState, xylanAVLRadiusAcctPort=xylanAVLRadiusAcctPort, xylanAVLRadiusAddress=xylanAVLRadiusAddress, xylanAVLpassprompt=xylanAVLpassprompt, xylanAVLRadiusAcctSecret=xylanAVLRadiusAcctSecret, xylanAVLLdapLoginFailId=xylanAVLLdapLoginFailId, xylanAVLauthmode=xylanAVLauthmode)
