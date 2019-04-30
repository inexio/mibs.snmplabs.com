#
# PySNMP MIB module ANS-ADMIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ANS-ADMIN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
RowPointer, mlpmpR115, RowStatus = mibBuilder.importSymbols("ANS-COMMON-MIB", "RowPointer", "mlpmpR115", "RowStatus")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, NotificationType, ModuleIdentity, Bits, TimeTicks, Counter64, Counter32, Gauge32, Integer32, MibIdentifier, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Bits", "TimeTicks", "Counter64", "Counter32", "Gauge32", "Integer32", "MibIdentifier", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adminServices = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 96, 115, 6))
ansLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1))
ansLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1), )
if mibBuilder.loadTexts: ansLicenseTable.setStatus('mandatory')
ansLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1), ).setIndexNames((0, "ANS-ADMIN-MIB", "ansLicenseId"))
if mibBuilder.loadTexts: ansLicenseEntry.setStatus('mandatory')
ansLicenseId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ansLicenseId.setStatus('mandatory')
ansLicenseName = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ansLicenseName.setStatus('mandatory')
ansLicenseCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ansLicenseCapacity.setStatus('mandatory')
ansLicenseCurrentCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ansLicenseCurrentCapacity.setStatus('mandatory')
ansLicenseExpirationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ansLicenseExpirationDate.setStatus('mandatory')
ansLicenseInstall = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 96, 115, 6, 1, 1, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ansLicenseInstall.setStatus('mandatory')
mibBuilder.exportSymbols("ANS-ADMIN-MIB", ansLicenseCurrentCapacity=ansLicenseCurrentCapacity, ansLicenseId=ansLicenseId, adminServices=adminServices, ansLicenseInstall=ansLicenseInstall, ansLicenseCapacity=ansLicenseCapacity, ansLicenseEntry=ansLicenseEntry, ansLicense=ansLicense, ansLicenseName=ansLicenseName, ansLicenseExpirationDate=ansLicenseExpirationDate, ansLicenseTable=ansLicenseTable)