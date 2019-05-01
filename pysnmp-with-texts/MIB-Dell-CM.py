#
# PySNMP MIB module MIB-Dell-CM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MIB-Dell-CM
# Produced by pysmi-0.3.4 at Wed May  1 14:11:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, Counter32, IpAddress, enterprises, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, ModuleIdentity, ObjectIdentity, Integer32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Counter32", "IpAddress", "enterprises", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Integer32", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dell = MibIdentifier((1, 3, 6, 1, 4, 1, 674))
cm = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10899))
inventoryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10899, 1))
operatingSystemGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10899, 2))
productID = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10899, 100))
class SystemID(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class Unsigned16BitRange(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

inventoryLocale = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryLocale.setStatus('mandatory')
if mibBuilder.loadTexts: inventoryLocale.setDescription('This attribute defines the locale for the system.')
inventorySchemaVersion = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventorySchemaVersion.setStatus('mandatory')
if mibBuilder.loadTexts: inventorySchemaVersion.setDescription('This attribute defines the version of the inventory schema implemented by this system.')
inventorySystemID = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 1, 3), SystemID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventorySystemID.setStatus('mandatory')
if mibBuilder.loadTexts: inventorySystemID.setDescription('This attribute defines the System ID for the system.')
deviceTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10899, 1, 5), )
if mibBuilder.loadTexts: deviceTable.setStatus('mandatory')
if mibBuilder.loadTexts: deviceTable.setDescription('This defines a table of versioned devices as inventoried by the product.')
deviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1), ).setIndexNames((0, "MIB-Dell-CM", "deviceIndex"))
if mibBuilder.loadTexts: deviceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: deviceEntry.setDescription('This defines a row of versioned devices as inventoried by the product.')
deviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 1), Unsigned16BitRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: deviceIndex.setDescription('This attribute defines the unique index for this device.')
deviceComponentID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceComponentID.setStatus('mandatory')
if mibBuilder.loadTexts: deviceComponentID.setDescription('This attribute defines an optional component id field for the device.')
deviceDisplayString = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDisplayString.setStatus('mandatory')
if mibBuilder.loadTexts: deviceDisplayString.setDescription('This attribute provides a displayable string that describes the device.')
deviceVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceVendorID.setStatus('mandatory')
if mibBuilder.loadTexts: deviceVendorID.setDescription('This attribute represents the ID for the vendor supplying the device.')
deviceDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDeviceID.setStatus('mandatory')
if mibBuilder.loadTexts: deviceDeviceID.setDescription('This attribute represents the ID for the device.')
deviceSubID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSubID.setStatus('mandatory')
if mibBuilder.loadTexts: deviceSubID.setDescription('This attribute provides additional device identification information.')
deviceSubVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10899, 1, 5, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSubVendorID.setStatus('mandatory')
if mibBuilder.loadTexts: deviceSubVendorID.setDescription('This attribute provides additional vendor identification information.')
applicationTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10899, 1, 6), )
if mibBuilder.loadTexts: applicationTable.setStatus('mandatory')
if mibBuilder.loadTexts: applicationTable.setDescription('This defines a table of application information for the system.')
applicationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1), ).setIndexNames((0, "MIB-Dell-CM", "applicationIndex"))
if mibBuilder.loadTexts: applicationEntry.setStatus('mandatory')
if mibBuilder.loadTexts: applicationEntry.setDescription('This defines a row of application information for the system.')
applicationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1, 1), Unsigned16BitRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applicationIndex.setStatus('mandatory')
if mibBuilder.loadTexts: applicationIndex.setDescription('This attribute defines the unique index for this application.')
applicationDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1, 2), Unsigned16BitRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applicationDeviceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: applicationDeviceIndex.setDescription('This attribute defines a cross-index to the device table for the application.')
applicationComponentType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applicationComponentType.setStatus('mandatory')
if mibBuilder.loadTexts: applicationComponentType.setDescription('This attribute identifies the type of application reported.')
applicationVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applicationVersion.setStatus('mandatory')
if mibBuilder.loadTexts: applicationVersion.setDescription('This attribute identifies the version of the application.')
applicationDisplayString = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applicationDisplayString.setStatus('mandatory')
if mibBuilder.loadTexts: applicationDisplayString.setDescription('This attribute provides a user visible display string that describes the application.')
applicationSubComponentID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10899, 1, 6, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applicationSubComponentID.setStatus('mandatory')
if mibBuilder.loadTexts: applicationSubComponentID.setDescription('This attribute provides the sub component id for the application. This is usually valid on ESM device reporting.')
operatingSystemVendor = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: operatingSystemVendor.setStatus('mandatory')
if mibBuilder.loadTexts: operatingSystemVendor.setDescription('This attribute defines the vendor of the Operating System.')
operatingSystemMajorVersion = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: operatingSystemMajorVersion.setStatus('mandatory')
if mibBuilder.loadTexts: operatingSystemMajorVersion.setDescription('This attribute defines the major version of the Operating System.')
operatingSystemMinorVersion = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: operatingSystemMinorVersion.setStatus('mandatory')
if mibBuilder.loadTexts: operatingSystemMinorVersion.setDescription('This attribute defines the minor version of the Operating System.')
operatingSystemSPMajorVersion = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: operatingSystemSPMajorVersion.setStatus('mandatory')
if mibBuilder.loadTexts: operatingSystemSPMajorVersion.setDescription("This attribute defines the Operating System's Service Pack major version.")
operatingSystemSPMinorVersion = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: operatingSystemSPMinorVersion.setStatus('mandatory')
if mibBuilder.loadTexts: operatingSystemSPMinorVersion.setDescription("This attribute defines the Operating System's Service Pack minor version.")
operatingSystemArchitecture = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: operatingSystemArchitecture.setStatus('mandatory')
if mibBuilder.loadTexts: operatingSystemArchitecture.setDescription("This attribute defines the Operating System's architecture.")
productIDDisplayName = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 100, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIDDisplayName.setStatus('mandatory')
if mibBuilder.loadTexts: productIDDisplayName.setDescription('This attribute defines the display name of the product.')
productIDDescription = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 100, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIDDescription.setStatus('mandatory')
if mibBuilder.loadTexts: productIDDescription.setDescription('This attribute defines a short description of the product.')
productIDVendor = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 100, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIDVendor.setStatus('mandatory')
if mibBuilder.loadTexts: productIDVendor.setDescription('This attribute defines the name of the manufacturer of the product.')
productIDVersion = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 100, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIDVersion.setStatus('mandatory')
if mibBuilder.loadTexts: productIDVersion.setDescription('This attribute defines the version of the product.')
productIDBuildNumber = MibScalar((1, 3, 6, 1, 4, 1, 674, 10899, 100, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productIDBuildNumber.setStatus('obsolete')
if mibBuilder.loadTexts: productIDBuildNumber.setDescription('This attribute defines the software build number of the product.')
mibBuilder.exportSymbols("MIB-Dell-CM", productIDBuildNumber=productIDBuildNumber, deviceEntry=deviceEntry, cm=cm, operatingSystemSPMinorVersion=operatingSystemSPMinorVersion, Unsigned16BitRange=Unsigned16BitRange, deviceVendorID=deviceVendorID, operatingSystemArchitecture=operatingSystemArchitecture, applicationTable=applicationTable, operatingSystemSPMajorVersion=operatingSystemSPMajorVersion, deviceIndex=deviceIndex, applicationDeviceIndex=applicationDeviceIndex, productIDVendor=productIDVendor, applicationEntry=applicationEntry, inventorySystemID=inventorySystemID, applicationSubComponentID=applicationSubComponentID, deviceSubID=deviceSubID, operatingSystemVendor=operatingSystemVendor, productIDDisplayName=productIDDisplayName, deviceSubVendorID=deviceSubVendorID, applicationVersion=applicationVersion, deviceDisplayString=deviceDisplayString, deviceDeviceID=deviceDeviceID, productIDDescription=productIDDescription, inventoryGroup=inventoryGroup, deviceComponentID=deviceComponentID, operatingSystemMajorVersion=operatingSystemMajorVersion, applicationComponentType=applicationComponentType, applicationDisplayString=applicationDisplayString, inventorySchemaVersion=inventorySchemaVersion, operatingSystemMinorVersion=operatingSystemMinorVersion, deviceTable=deviceTable, applicationIndex=applicationIndex, SystemID=SystemID, productIDVersion=productIDVersion, dell=dell, productID=productID, inventoryLocale=inventoryLocale, operatingSystemGroup=operatingSystemGroup)
