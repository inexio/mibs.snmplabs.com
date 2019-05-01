#
# PySNMP MIB module INTEL-VAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-VAS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:54:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, IpAddress, ModuleIdentity, ObjectIdentity, Unsigned32, iso, NotificationType, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "iso", "NotificationType", "MibIdentifier", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vas = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 53))
vasConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 53, 1))
vasConfigTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1), )
if mibBuilder.loadTexts: vasConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: vasConfigTable.setDescription('VAS record')
vasConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1), ).setIndexNames((0, "INTEL-VAS-MIB", "vasConfigIndex"))
if mibBuilder.loadTexts: vasConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vasConfigEntry.setDescription('')
vasConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vasConfigIndex.setStatus('mandatory')
if mibBuilder.loadTexts: vasConfigIndex.setDescription('This is an index of the feature')
vasConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vasConfigStatus.setStatus('mandatory')
if mibBuilder.loadTexts: vasConfigStatus.setDescription('Holds status of feature. ZERO for OFF, NON-ZERO for On')
vasConfigLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vasConfigLicenseKey.setStatus('mandatory')
if mibBuilder.loadTexts: vasConfigLicenseKey.setDescription('This is the raw ascii license key, C-string')
vasConfigNameOfLicense = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vasConfigNameOfLicense.setStatus('mandatory')
if mibBuilder.loadTexts: vasConfigNameOfLicense.setDescription('Name of the actual license, ex OSPF, C-string')
vasConfigEraseLicense = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vasConfigEraseLicense.setStatus('mandatory')
if mibBuilder.loadTexts: vasConfigEraseLicense.setDescription('Write clears the license key. Read returns granularity of license')
vasConfigDemoLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vasConfigDemoLicenseKey.setStatus('mandatory')
if mibBuilder.loadTexts: vasConfigDemoLicenseKey.setDescription('Number of hours for this license key to operate, ZERO means no limit')
vasConfigNameOfUser = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vasConfigNameOfUser.setStatus('mandatory')
if mibBuilder.loadTexts: vasConfigNameOfUser.setDescription('Name of user, C-string')
vasConfigDateOfIssue = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 53, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vasConfigDateOfIssue.setStatus('mandatory')
if mibBuilder.loadTexts: vasConfigDateOfIssue.setDescription('Date of issue as: YYYY-MM-DD, C-string')
mibBuilder.exportSymbols("INTEL-VAS-MIB", vasConfig=vasConfig, vasConfigNameOfUser=vasConfigNameOfUser, vasConfigIndex=vasConfigIndex, vasConfigEraseLicense=vasConfigEraseLicense, vasConfigTable=vasConfigTable, vas=vas, vasConfigDemoLicenseKey=vasConfigDemoLicenseKey, vasConfigEntry=vasConfigEntry, vasConfigLicenseKey=vasConfigLicenseKey, vasConfigDateOfIssue=vasConfigDateOfIssue, vasConfigNameOfLicense=vasConfigNameOfLicense, vasConfigStatus=vasConfigStatus)
