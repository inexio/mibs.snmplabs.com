#
# PySNMP MIB module HUAWEI-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:48:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
huaweiUtility, = mibBuilder.importSymbols("HUAWEI-MIB", "huaweiUtility")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, MibIdentifier, Unsigned32, NotificationType, Counter64, TimeTicks, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "MibIdentifier", "Unsigned32", "NotificationType", "Counter64", "TimeTicks", "ModuleIdentity", "IpAddress")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
syslogMIBObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 6, 35))
if mibBuilder.loadTexts: syslogMIBObjects.setLastUpdated('200404240900Z')
if mibBuilder.loadTexts: syslogMIBObjects.setOrganization('Fix-Net Dept, Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: syslogMIBObjects.setContactInfo('Floor 5, Block 4, R&D Building, Huawei Longgang Production Base, Shenzhen, P.R.C. http://www.huawei.com Zip: 518129 ')
if mibBuilder.loadTexts: syslogMIBObjects.setDescription('The MIB contains objects of system log.')
syslogEnableAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 35, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogEnableAdminStatus.setStatus('current')
if mibBuilder.loadTexts: syslogEnableAdminStatus.setDescription(' The board supports the configuration of switch group of system log server. The configuration mode can be bit-domain setting, board is numbered 1 to 18, correspondingly to the bit of BIT1 to BIT18, 1 means enable, 0 means disable. ')
syslogServerTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 6, 35, 2), )
if mibBuilder.loadTexts: syslogServerTable.setStatus('current')
if mibBuilder.loadTexts: syslogServerTable.setDescription(' The system log server table. ')
syslogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 6, 35, 2, 1), ).setIndexNames((0, "HUAWEI-SYSLOG-MIB", "syslogServerIpAddress"))
if mibBuilder.loadTexts: syslogServerEntry.setStatus('current')
if mibBuilder.loadTexts: syslogServerEntry.setDescription(' The entry of the system log server table. ')
syslogServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 35, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogServerIpAddress.setStatus('current')
if mibBuilder.loadTexts: syslogServerIpAddress.setDescription(' The IP address of system log server ')
syslogPolicyGroupNameSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 35, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogPolicyGroupNameSelect.setStatus('current')
if mibBuilder.loadTexts: syslogPolicyGroupNameSelect.setDescription(' The name of policy group selected by the system log server, one server can only use one policy server group. ')
syslogServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 35, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: syslogServerRowStatus.setDescription(' The row status, used to add and delete. ')
syslogPolicyGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 6, 35, 3), )
if mibBuilder.loadTexts: syslogPolicyGroupTable.setStatus('current')
if mibBuilder.loadTexts: syslogPolicyGroupTable.setDescription('The policy group control table.')
syslogPolicyGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 6, 35, 3, 1), ).setIndexNames((0, "HUAWEI-SYSLOG-MIB", "syslogPolicyGroupName"))
if mibBuilder.loadTexts: syslogPolicyGroupEntry.setStatus('current')
if mibBuilder.loadTexts: syslogPolicyGroupEntry.setDescription('The entry of policy group control table.')
syslogPolicyGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 35, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogPolicyGroupName.setStatus('current')
if mibBuilder.loadTexts: syslogPolicyGroupName.setDescription(' The name of policy group. ')
syslogPolicyGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 35, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogPolicyGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: syslogPolicyGroupRowStatus.setDescription(' The row status of policy group, used to add and delete.')
syslogPolicyConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 6, 35, 4), )
if mibBuilder.loadTexts: syslogPolicyConfigTable.setStatus('current')
if mibBuilder.loadTexts: syslogPolicyConfigTable.setDescription(' The system server policy config table. ')
syslogPolicyConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1), ).setIndexNames((0, "HUAWEI-SYSLOG-MIB", "syslogPolicyConfigIndex"))
if mibBuilder.loadTexts: syslogPolicyConfigEntry.setStatus('current')
if mibBuilder.loadTexts: syslogPolicyConfigEntry.setDescription(' The entry of system server policy config table.')
syslogPolicyConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: syslogPolicyConfigIndex.setStatus('current')
if mibBuilder.loadTexts: syslogPolicyConfigIndex.setDescription(' The index of system log policy config. ')
syslogPolicyDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogPolicyDescr.setStatus('current')
if mibBuilder.loadTexts: syslogPolicyDescr.setDescription(' The description of policy. ')
syslogUserType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 101, 102, 200))).clone(namedValues=NamedValues(("all", 0), ("portal", 1), ("ppp", 2), ("l2static", 3), ("l2dynamic", 4), ("l3", 5), ("l2tp", 6), ("telnet", 7), ("dot1x", 101), ("wlan", 102), ("others", 200)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogUserType.setStatus('current')
if mibBuilder.loadTexts: syslogUserType.setDescription(' Filtrating the system log information of different user type. ')
syslogPolicyBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 4), Bits().clone(namedValues=NamedValues(("first", 1), ("second", 2), ("third", 3), ("fouth", 4), ("fifth", 5), ("sixth", 6), ("seventh", 7), ("eighth", 8), ("ninth", 9), ("tenth", 10), ("eleventh", 11), ("twelfth", 12), ("thirteenth", 13), ("fourteenth", 14), ("fifteenth", 15), ("sixteenth", 16), ("seventennth", 17), ("eighteenth", 18)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogPolicyBoard.setStatus('current')
if mibBuilder.loadTexts: syslogPolicyBoard.setDescription(' The board which policy taking effect. ')
syslogPolicyIsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 5), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogPolicyIsp.setStatus('current')
if mibBuilder.loadTexts: syslogPolicyIsp.setDescription(" The selection of ISP, the null character means tracing operation log of all ISP. More than one ISP can be separated by character ';', for example, if the policy can support 2 ISPs, it can express as ISP1; ISP2. ")
syslogPolicyType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("all", 1), ("userOperSyslog", 2), ("callSyslog", 3))).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogPolicyType.setStatus('current')
if mibBuilder.loadTexts: syslogPolicyType.setDescription(' The selection of system log filter type. ')
syslogGroupChoice = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogGroupChoice.setStatus('current')
if mibBuilder.loadTexts: syslogGroupChoice.setDescription(" The server group which the policy belongs to. When one policy belongs to more than one policy server group, name of policy server group can be separated by character ';'. ")
syslogPolicyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogPolicyRowStatus.setStatus('current')
if mibBuilder.loadTexts: syslogPolicyRowStatus.setDescription(' The row status, used to add and delete. ')
hwSyslogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 35, 100))
hwSyslogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 1))
hwSyslogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 1, 1)).setObjects(("HUAWEI-SYSLOG-MIB", "hwSyslogAdminStatusObjectGroup"), ("HUAWEI-SYSLOG-MIB", "hwSyslogServerObjectGroup"), ("HUAWEI-SYSLOG-MIB", "hwSyslogPolicyGroupObjectGroup"), ("HUAWEI-SYSLOG-MIB", "hwSyslogPolicyConfigObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSyslogCompliance = hwSyslogCompliance.setStatus('current')
if mibBuilder.loadTexts: hwSyslogCompliance.setDescription('The compliance statement for systems supporting the this module.')
hwSyslogObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 2))
hwSyslogAdminStatusObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 2, 1)).setObjects(("HUAWEI-SYSLOG-MIB", "syslogEnableAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSyslogAdminStatusObjectGroup = hwSyslogAdminStatusObjectGroup.setStatus('current')
if mibBuilder.loadTexts: hwSyslogAdminStatusObjectGroup.setDescription('The system log administrate status group.')
hwSyslogServerObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 2, 2)).setObjects(("HUAWEI-SYSLOG-MIB", "syslogServerIpAddress"), ("HUAWEI-SYSLOG-MIB", "syslogPolicyGroupNameSelect"), ("HUAWEI-SYSLOG-MIB", "syslogServerRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSyslogServerObjectGroup = hwSyslogServerObjectGroup.setStatus('current')
if mibBuilder.loadTexts: hwSyslogServerObjectGroup.setDescription('The system log server group.')
hwSyslogPolicyGroupObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 2, 3)).setObjects(("HUAWEI-SYSLOG-MIB", "syslogPolicyGroupName"), ("HUAWEI-SYSLOG-MIB", "syslogPolicyGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSyslogPolicyGroupObjectGroup = hwSyslogPolicyGroupObjectGroup.setStatus('current')
if mibBuilder.loadTexts: hwSyslogPolicyGroupObjectGroup.setDescription('The system log policy group.')
hwSyslogPolicyConfigObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 2, 4)).setObjects(("HUAWEI-SYSLOG-MIB", "syslogPolicyDescr"), ("HUAWEI-SYSLOG-MIB", "syslogUserType"), ("HUAWEI-SYSLOG-MIB", "syslogPolicyBoard"), ("HUAWEI-SYSLOG-MIB", "syslogPolicyIsp"), ("HUAWEI-SYSLOG-MIB", "syslogPolicyType"), ("HUAWEI-SYSLOG-MIB", "syslogGroupChoice"), ("HUAWEI-SYSLOG-MIB", "syslogPolicyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSyslogPolicyConfigObjectGroup = hwSyslogPolicyConfigObjectGroup.setStatus('current')
if mibBuilder.loadTexts: hwSyslogPolicyConfigObjectGroup.setDescription('The system log policy config group.')
mibBuilder.exportSymbols("HUAWEI-SYSLOG-MIB", syslogPolicyType=syslogPolicyType, syslogServerEntry=syslogServerEntry, syslogPolicyIsp=syslogPolicyIsp, syslogPolicyGroupRowStatus=syslogPolicyGroupRowStatus, syslogPolicyGroupTable=syslogPolicyGroupTable, syslogGroupChoice=syslogGroupChoice, hwSyslogPolicyConfigObjectGroup=hwSyslogPolicyConfigObjectGroup, hwSyslogPolicyGroupObjectGroup=hwSyslogPolicyGroupObjectGroup, syslogMIBObjects=syslogMIBObjects, syslogPolicyGroupNameSelect=syslogPolicyGroupNameSelect, syslogPolicyRowStatus=syslogPolicyRowStatus, hwSyslogServerObjectGroup=hwSyslogServerObjectGroup, syslogPolicyConfigEntry=syslogPolicyConfigEntry, syslogServerIpAddress=syslogServerIpAddress, hwSyslogObjectGroups=hwSyslogObjectGroups, syslogServerRowStatus=syslogServerRowStatus, syslogEnableAdminStatus=syslogEnableAdminStatus, syslogPolicyBoard=syslogPolicyBoard, hwSyslogConformance=hwSyslogConformance, syslogPolicyGroupName=syslogPolicyGroupName, hwSyslogCompliance=hwSyslogCompliance, syslogUserType=syslogUserType, hwSyslogAdminStatusObjectGroup=hwSyslogAdminStatusObjectGroup, syslogPolicyDescr=syslogPolicyDescr, PYSNMP_MODULE_ID=syslogMIBObjects, syslogPolicyConfigIndex=syslogPolicyConfigIndex, hwSyslogCompliances=hwSyslogCompliances, syslogPolicyConfigTable=syslogPolicyConfigTable, syslogPolicyGroupEntry=syslogPolicyGroupEntry, syslogServerTable=syslogServerTable)
