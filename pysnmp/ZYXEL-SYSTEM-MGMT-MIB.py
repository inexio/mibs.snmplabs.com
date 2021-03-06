#
# PySNMP MIB module ZYXEL-SYSTEM-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-SYSTEM-MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:45:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter64, ObjectIdentity, ModuleIdentity, Integer32, Counter32, MibIdentifier, Bits, NotificationType, iso, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "ObjectIdentity", "ModuleIdentity", "Integer32", "Counter32", "MibIdentifier", "Bits", "NotificationType", "iso", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49))
if mibBuilder.loadTexts: zyxelManagement.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelManagement.setOrganization('Enterprise Solution ZyXEL')
zyxelSysMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1))
zyxelSysMgmtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 2))
zySysMgmtConfigSave = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("config1", 1), ("config2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtConfigSave.setStatus('current')
zySysMgmtBootupConfig = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("config1", 1), ("config2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtBootupConfig.setStatus('current')
zySysMgmtReboot = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nothing", 0), ("reboot", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtReboot.setStatus('current')
zySysMgmtDefaultConfig = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nothing", 0), ("resetToDefault", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtDefaultConfig.setStatus('current')
zySysMgmtLastActionStatus = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("success", 1), ("fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysMgmtLastActionStatus.setStatus('current')
zySysMgmtSysStatus = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 6), Bits().clone(namedValues=NamedValues(("sysAlarmDetected", 0), ("sysTemperatureError", 1), ("sysFanRPMError", 2), ("sysVoltageRangeError", 3), ("sysNoDefect", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysMgmtSysStatus.setStatus('current')
zySysMgmtCPUUsage = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysMgmtCPUUsage.setStatus('current')
zySysMgmtBootupImage = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("image1", 1), ("image2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtBootupImage.setStatus('current')
zySysMgmtCounterReset = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtCounterReset.setStatus('current')
zyxelSysMgmtTftpServiceSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10))
zySysMgmtTftpServiceServerIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtTftpServiceServerIpAddress.setStatus('current')
zySysMgmtTftpRemoteFileName = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtTftpRemoteFileName.setStatus('current')
zySysMgmtTftpConfigIndex = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("config1", 1), ("config2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtTftpConfigIndex.setStatus('current')
zySysMgmtTftpAction = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("backupConfig", 1), ("restoreConfig", 2), ("mergeConfig", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtTftpAction.setStatus('current')
zySysMgmtTftpActionStatus = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("success", 1), ("fail", 2), ("underAction", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysMgmtTftpActionStatus.setStatus('current')
zySysMgmtTftpActionPrivilege13 = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 113), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("backupConfig", 1), ("restoreConfig", 2), ("mergeConfig", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtTftpActionPrivilege13.setStatus('current')
zySysMgmtReloadFactoryDefault = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nothing", 0), ("reloadFactoryDefault", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtReloadFactoryDefault.setStatus('current')
zySysMgmtReloadStackingDefault = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nothing", 0), ("reloadStackingDefault", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtReloadStackingDefault.setStatus('current')
zySysMgmtConfigSavePrivilege13 = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 113), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("config1", 1), ("config2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtConfigSavePrivilege13.setStatus('current')
zySysMgmtDefaultConfigPrivilege13 = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 213), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nothing", 0), ("resetToDefault", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySysMgmtDefaultConfigPrivilege13.setStatus('current')
zySysMgmtUncontrolledSystemReset = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 2, 1))
if mibBuilder.loadTexts: zySysMgmtUncontrolledSystemReset.setStatus('current')
zySysMgmtControlledSystemReset = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 2, 2))
if mibBuilder.loadTexts: zySysMgmtControlledSystemReset.setStatus('current')
zySysMgmtBootImageInconsistence = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 2, 3))
if mibBuilder.loadTexts: zySysMgmtBootImageInconsistence.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-SYSTEM-MGMT-MIB", zyxelManagement=zyxelManagement, zySysMgmtReboot=zySysMgmtReboot, PYSNMP_MODULE_ID=zyxelManagement, zySysMgmtCounterReset=zySysMgmtCounterReset, zySysMgmtTftpAction=zySysMgmtTftpAction, zySysMgmtTftpActionStatus=zySysMgmtTftpActionStatus, zySysMgmtTftpServiceServerIpAddress=zySysMgmtTftpServiceServerIpAddress, zySysMgmtReloadFactoryDefault=zySysMgmtReloadFactoryDefault, zyxelSysMgmt=zyxelSysMgmt, zySysMgmtControlledSystemReset=zySysMgmtControlledSystemReset, zySysMgmtTftpRemoteFileName=zySysMgmtTftpRemoteFileName, zySysMgmtReloadStackingDefault=zySysMgmtReloadStackingDefault, zyxelSysMgmtTftpServiceSetup=zyxelSysMgmtTftpServiceSetup, zySysMgmtConfigSave=zySysMgmtConfigSave, zySysMgmtConfigSavePrivilege13=zySysMgmtConfigSavePrivilege13, zySysMgmtUncontrolledSystemReset=zySysMgmtUncontrolledSystemReset, zySysMgmtBootupConfig=zySysMgmtBootupConfig, zySysMgmtTftpConfigIndex=zySysMgmtTftpConfigIndex, zySysMgmtTftpActionPrivilege13=zySysMgmtTftpActionPrivilege13, zySysMgmtBootImageInconsistence=zySysMgmtBootImageInconsistence, zySysMgmtCPUUsage=zySysMgmtCPUUsage, zySysMgmtSysStatus=zySysMgmtSysStatus, zySysMgmtBootupImage=zySysMgmtBootupImage, zySysMgmtDefaultConfig=zySysMgmtDefaultConfig, zySysMgmtLastActionStatus=zySysMgmtLastActionStatus, zySysMgmtDefaultConfigPrivilege13=zySysMgmtDefaultConfigPrivilege13, zyxelSysMgmtNotifications=zyxelSysMgmtNotifications)
