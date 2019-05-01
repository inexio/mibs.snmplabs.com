#
# PySNMP MIB module RUCKUS-HWINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-HWINFO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:58:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ruckusCommonHwInfoModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonHwInfoModule")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, ModuleIdentity, Integer32, Counter64, Bits, IpAddress, Counter32, Gauge32, MibIdentifier, ObjectIdentity, Unsigned32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Integer32", "Counter64", "Bits", "IpAddress", "Counter32", "Gauge32", "MibIdentifier", "ObjectIdentity", "Unsigned32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ruckusHwInfoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1))
if mibBuilder.loadTexts: ruckusHwInfoMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusHwInfoMIB.setOrganization('Ruckus Wireless, Inc.')
if mibBuilder.loadTexts: ruckusHwInfoMIB.setContactInfo('Ruckus Wireless Inc. Postal: 880 W Maude Ave Sunnyvale, CA 94085 USA EMail: support@ruckuswireless.com Phone: +1-650-265-4200')
if mibBuilder.loadTexts: ruckusHwInfoMIB.setDescription('Ruckus hardware information objects.')
ruckusHwInfoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1))
ruckusHwInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1))
ruckusHwInfoEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 2))
ruckusHwInfoModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusHwInfoModelNumber.setStatus('current')
if mibBuilder.loadTexts: ruckusHwInfoModelNumber.setDescription('Specifies the model number of the device.')
ruckusHwInfoSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusHwInfoSerialNumber.setStatus('current')
if mibBuilder.loadTexts: ruckusHwInfoSerialNumber.setDescription('Specifies the serial number of the device.')
ruckusHwInfoCustomerID = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusHwInfoCustomerID.setStatus('current')
if mibBuilder.loadTexts: ruckusHwInfoCustomerID.setDescription('Specifies the name of the customer.')
ruckusHwInfoHWMajorRevision = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusHwInfoHWMajorRevision.setStatus('current')
if mibBuilder.loadTexts: ruckusHwInfoHWMajorRevision.setDescription('Specifies major hardware revision.')
ruckusHwInfoHWMinorRevision = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusHwInfoHWMinorRevision.setStatus('current')
if mibBuilder.loadTexts: ruckusHwInfoHWMinorRevision.setDescription('Specifies minor hardware revision.')
mibBuilder.exportSymbols("RUCKUS-HWINFO-MIB", ruckusHwInfoHWMinorRevision=ruckusHwInfoHWMinorRevision, ruckusHwInfoCustomerID=ruckusHwInfoCustomerID, ruckusHwInfoModelNumber=ruckusHwInfoModelNumber, ruckusHwInfoHWMajorRevision=ruckusHwInfoHWMajorRevision, PYSNMP_MODULE_ID=ruckusHwInfoMIB, ruckusHwInfoObjects=ruckusHwInfoObjects, ruckusHwInfoMIB=ruckusHwInfoMIB, ruckusHwInfoSerialNumber=ruckusHwInfoSerialNumber, ruckusHwInfo=ruckusHwInfo, ruckusHwInfoEvents=ruckusHwInfoEvents)
