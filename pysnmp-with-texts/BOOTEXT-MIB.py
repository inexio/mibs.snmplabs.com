#
# PySNMP MIB module BOOTEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BOOTEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:40:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bootExt, = mibBuilder.importSymbols("APENT-MIB", "bootExt")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, TimeTicks, Bits, Counter32, ObjectIdentity, ModuleIdentity, Counter64, Gauge32, Unsigned32, MibIdentifier, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Bits", "Counter32", "ObjectIdentity", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "MibIdentifier", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bootExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 31, 1))
if mibBuilder.loadTexts: bootExtMib.setLastUpdated('9801282000Z')
if mibBuilder.loadTexts: bootExtMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: bootExtMib.setContactInfo('Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: bootExtMib.setDescription('This MIB module describes the ArrowPoint enterprise MIB support for system boot adminstration')
apBootBootP = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootBootP.setStatus('current')
if mibBuilder.loadTexts: apBootBootP.setDescription('This variable controls whether the system will use BOOTP. This object is NOT-CURRENTLY-SUPPORTED')
apBootIpOfSystem = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootIpOfSystem.setStatus('current')
if mibBuilder.loadTexts: apBootIpOfSystem.setDescription('The IP address the system will use at boot time. If BOOTP is enabled, this object will be overridden')
apBootPrimaryType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("boot-from-disk", 1), ("boot-via-ftp", 2), ("boot-via-network", 3), ("not-configured", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootPrimaryType.setStatus('current')
if mibBuilder.loadTexts: apBootPrimaryType.setDescription('This object controls the primary mechansim for booting the system. boot-via-disk Boot an installed ADI boot-via-ftp Boot an FTP resident ADI and install boot-via-network Boot from a network drive')
apBootPrimaryFileName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootPrimaryFileName.setStatus('current')
if mibBuilder.loadTexts: apBootPrimaryFileName.setDescription('File name associated with primary boot record if boot-via-disk or boot-via-ftp. If boot-via-disk, this name is the installed ADI to boot. If boot-via-ftp, this name is the FTP resident ADI which will be installed.')
apBootPrimaryFTPRecordName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootPrimaryFTPRecordName.setStatus('current')
if mibBuilder.loadTexts: apBootPrimaryFTPRecordName.setDescription('FTP record name associated with primary boot, only valid if apBootPrimaryType designated as boot-via-ftp or boot-via-network')
apBootSecondaryType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("boot-from-disk", 1), ("boot-via-ftp", 2), ("boot-via-network", 3), ("not-configured", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootSecondaryType.setStatus('current')
if mibBuilder.loadTexts: apBootSecondaryType.setDescription('This object controls the secondary mechansim for booting the system')
apBootSecondaryFileName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootSecondaryFileName.setStatus('current')
if mibBuilder.loadTexts: apBootSecondaryFileName.setDescription('File name associated with secondary boot record. See description for apBootPrimaryFileName')
apBootSecondaryFTPRecordName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootSecondaryFTPRecordName.setStatus('current')
if mibBuilder.loadTexts: apBootSecondaryFTPRecordName.setDescription('FTP record name associated with secondary boot, only valid if apBootSecondaryType designated as boot-via-ftp or boot-via-network')
apBootLastType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("boot-from-disk", 1), ("boot-via-ftp", 2), ("boot-via-network", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBootLastType.setStatus('current')
if mibBuilder.loadTexts: apBootLastType.setDescription('The last successful boot type')
apBootLastFileName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBootLastFileName.setStatus('current')
if mibBuilder.loadTexts: apBootLastFileName.setDescription('File name associated with the last successful boot')
apBootLastFTPRecordName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBootLastFTPRecordName.setStatus('current')
if mibBuilder.loadTexts: apBootLastFTPRecordName.setDescription('FTP record name associated with last boot, only valid if apBootLastType designated as boot-via-ftp')
apBootNetmaskOfSystem = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 13), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootNetmaskOfSystem.setStatus('current')
if mibBuilder.loadTexts: apBootNetmaskOfSystem.setDescription('The network mask the system will use at boot time. If BOOTP is enabled, this object will be overridden')
apBootRedundantBootP = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantBootP.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantBootP.setDescription('This variable controls whether the system will use BOOTP')
apBootRedundantIpOfSystem = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantIpOfSystem.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantIpOfSystem.setDescription('The IP address the system will use at boot time. If BOOTP is enabled, this object will be overridden')
apBootRedundantPrimaryType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("boot-from-disk", 1), ("boot-via-ftp", 2), ("boot-via-network", 3), ("not-configured", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantPrimaryType.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantPrimaryType.setDescription('This object controls the primary mechansim for booting the system')
apBootRedundantPrimaryFileName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantPrimaryFileName.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantPrimaryFileName.setDescription('File name associated with primary boot record')
apBootRedundantPrimaryFTPRecordName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantPrimaryFTPRecordName.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantPrimaryFTPRecordName.setDescription('FTP record name associated with primary boot, only valid if apBootPrimaryType designated as boot-via-ftp')
apBootRedundantSecondaryType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("boot-from-disk", 1), ("boot-via-ftp", 2), ("boot-via-network", 3), ("not-configured", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantSecondaryType.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantSecondaryType.setDescription('This object controls the secondary mechansim for booting the system')
apBootRedundantSecondaryFileName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantSecondaryFileName.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantSecondaryFileName.setDescription('File name associated with secondary boot record')
apBootRedundantSecondaryFTPRecordName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantSecondaryFTPRecordName.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantSecondaryFTPRecordName.setDescription('FTP record name associated with secondary boot, only valid if apBootSecondaryType designated as boot-via-ftp')
apBootRedundantLastType = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("boot-from-disk", 1), ("boot-via-ftp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBootRedundantLastType.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantLastType.setDescription('The last successful boot type')
apBootRedundantLastFileName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBootRedundantLastFileName.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantLastFileName.setDescription('File name associated with the last successful boot')
apBootRedundantLastFTPRecordName = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBootRedundantLastFTPRecordName.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantLastFTPRecordName.setDescription('FTP record name associated with last boot, only valid if apBootLasyType designated as boot-via-ftp')
apBootRedundantNetmaskOfSystem = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 25), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantNetmaskOfSystem.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantNetmaskOfSystem.setDescription('The network mask the system will use at boot time. If BOOTP is enabled, this object will be overridden')
apBootPrimaryAltCfgPath = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootPrimaryAltCfgPath.setStatus('current')
if mibBuilder.loadTexts: apBootPrimaryAltCfgPath.setDescription('FTP record name with the Primary boot record for alternative configuration file location. May only be used in conjunction with boot-via-network.')
apBootSecondaryAltCfgPath = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootSecondaryAltCfgPath.setStatus('current')
if mibBuilder.loadTexts: apBootSecondaryAltCfgPath.setDescription('FTP record name with the Primary boot record for alternative configuration file location. May only be used in conjunction with boot-via-network.')
apBootRedundantPrimaryAltCfgPath = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantPrimaryAltCfgPath.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantPrimaryAltCfgPath.setDescription('FTP record name with the Primary boot record for alternative configuration file location. May only be used in conjunction with boot-via-network.')
apBootRedundantSecondaryAltCfgPath = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 31, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBootRedundantSecondaryAltCfgPath.setStatus('current')
if mibBuilder.loadTexts: apBootRedundantSecondaryAltCfgPath.setDescription('FTP record name with the Primary boot record for alternative configuration file location. May only be used in conjunction with boot-via-network.')
mibBuilder.exportSymbols("BOOTEXT-MIB", apBootPrimaryFileName=apBootPrimaryFileName, apBootLastType=apBootLastType, apBootRedundantIpOfSystem=apBootRedundantIpOfSystem, apBootBootP=apBootBootP, apBootSecondaryFileName=apBootSecondaryFileName, apBootLastFTPRecordName=apBootLastFTPRecordName, apBootRedundantPrimaryType=apBootRedundantPrimaryType, apBootNetmaskOfSystem=apBootNetmaskOfSystem, apBootRedundantPrimaryAltCfgPath=apBootRedundantPrimaryAltCfgPath, apBootRedundantNetmaskOfSystem=apBootRedundantNetmaskOfSystem, apBootRedundantLastFileName=apBootRedundantLastFileName, apBootRedundantPrimaryFileName=apBootRedundantPrimaryFileName, apBootSecondaryAltCfgPath=apBootSecondaryAltCfgPath, apBootRedundantPrimaryFTPRecordName=apBootRedundantPrimaryFTPRecordName, apBootPrimaryFTPRecordName=apBootPrimaryFTPRecordName, PYSNMP_MODULE_ID=bootExtMib, apBootPrimaryType=apBootPrimaryType, apBootRedundantBootP=apBootRedundantBootP, bootExtMib=bootExtMib, apBootRedundantSecondaryFileName=apBootRedundantSecondaryFileName, apBootRedundantSecondaryFTPRecordName=apBootRedundantSecondaryFTPRecordName, apBootRedundantLastFTPRecordName=apBootRedundantLastFTPRecordName, apBootRedundantLastType=apBootRedundantLastType, apBootRedundantSecondaryType=apBootRedundantSecondaryType, apBootLastFileName=apBootLastFileName, apBootRedundantSecondaryAltCfgPath=apBootRedundantSecondaryAltCfgPath, apBootPrimaryAltCfgPath=apBootPrimaryAltCfgPath, apBootSecondaryType=apBootSecondaryType, apBootIpOfSystem=apBootIpOfSystem, apBootSecondaryFTPRecordName=apBootSecondaryFTPRecordName)
