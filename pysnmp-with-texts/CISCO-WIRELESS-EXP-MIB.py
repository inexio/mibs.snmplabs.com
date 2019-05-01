#
# PySNMP MIB module CISCO-WIRELESS-EXP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WIRELESS-EXP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:21:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Counter64, ObjectIdentity, ModuleIdentity, Counter32, Bits, MibIdentifier, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Counter64", "ObjectIdentity", "ModuleIdentity", "Counter32", "Bits", "MibIdentifier", "Unsigned32", "iso")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
ciscoWirelessExpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 52))
ciscoWirelessExpMIB.setRevisions(('2005-12-27 10:03', '1999-05-13 20:10',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWirelessExpMIB.setRevisionsDescriptions(('Imported Unsigned32 from SNMPv2-SMI.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWirelessExpMIB.setLastUpdated('200512271003Z')
if mibBuilder.loadTexts: ciscoWirelessExpMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoWirelessExpMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: firestar-sw@cisco.com')
if mibBuilder.loadTexts: ciscoWirelessExpMIB.setDescription("This is the MIB Module for the Cisco Wireless Radio Point to Point experimental components. Glossary The following terms are used in the MIB definitions below. Radio Card: The line card that provides the wireless communication features. Radio Link: The bi-directional wireless link that exists between two communicating radio cards. Radio PHY: Represents the transmission characteristics of the Radio Link. RF Unit: The Radio Frequency components and the associated antennas. Radio System: Radio card and RF unit(s). Cisco Wireless Radio Experimental MIB Organization The Cisco Wireless Radio Experimental MIB provides the following management groups : When the draft-ietf-entmib-v2-03.txt gets finalized the Radio Frequency Group will be moved into that MIB. When the CISCO-IMAGE-MIB.my gets updated to include the image capabilities, the Image Group will be migrated into that MIB. When the CISCO-LED-MIB.my becomes available and supports the functionality the LED group needs, the LED group will be migrated into that. o. Radio Frequency Resource Group This contains information about the Radio frequency transmission and reception resources available on the system. This group determines the portions of the radio spectrum at which the radio subsystem can operate. This group in conjunction with the radio PHY group determine the acutal spectrum that gets used for communications. o. Image Group This provides facilities to manage radio line card's firmware image file URL's in router's image repository. It also provides access to the image details. o. LED Group This group provides information about LEDs available on the line card. o. Duplexor Group This group provides information about the Duplexors installed in the RF resources.")
cwrRadioExpMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 52, 1))
cwrRadioFreqEntityGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1))
cwrRadioImageGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2))
cwrRadioLedGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3))
cwrRadioDuplexorGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4))
cwrRfEntityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1), )
if mibBuilder.loadTexts: cwrRfEntityTable.setStatus('current')
if mibBuilder.loadTexts: cwrRfEntityTable.setDescription('This table contains information about the radio frequency resources available for use on the system.')
cwrRfEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WIRELESS-EXP-MIB", "cwrRfEntityIndex"))
if mibBuilder.loadTexts: cwrRfEntityEntry.setStatus('current')
if mibBuilder.loadTexts: cwrRfEntityEntry.setDescription("This represents one entry in the cwrRfEntityTable. This table is largely a read only table which provides details on the radio frequency resources available on the system. Physically each RF resource may be realized by one antenna and its associated control hardware. But a single antenna and its associated hardware may act as more than 1 RF resource. A Duplexor is a mechanical device, that acts as a band pass filter when installed in an RF resource. Normally a RF resource is capable of operating over a wide frequency range. To operate at restricted frequencies, the user has to own that part of the frequency spectrum. Since the user may not own parts of the frequency spectrum over which the RF resource may operate, a Duplexor is installed in the RF resource. This restricts the RF resource to operate in the passband defined by the Duplexor. In this table the Duplexor's are identified by an index into the cwrDuplexorTable. It is indexed by the ifIndex and cwrRfEntityIndex.")
cwrRfEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cwrRfEntityIndex.setStatus('current')
if mibBuilder.loadTexts: cwrRfEntityIndex.setDescription('This object represents the index of this entry in the cwrRfEntityTable.')
cwrRfSwRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrRfSwRevision.setStatus('current')
if mibBuilder.loadTexts: cwrRfSwRevision.setDescription('This object represents the software revision number of controlling the RF subsystem.')
cwrRfAssemblyPartNumberClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrRfAssemblyPartNumberClass.setStatus('current')
if mibBuilder.loadTexts: cwrRfAssemblyPartNumberClass.setDescription('This object represents the assembly part number class of the RF subsystem.')
cwrRfAssemblyPartNumberBase = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrRfAssemblyPartNumberBase.setStatus('current')
if mibBuilder.loadTexts: cwrRfAssemblyPartNumberBase.setDescription('This object represents the assembly part number base of the RF subsystem.')
cwrRfAssemblyPartNumberVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrRfAssemblyPartNumberVersion.setStatus('current')
if mibBuilder.loadTexts: cwrRfAssemblyPartNumberVersion.setDescription('This object represents the assembly part number version of the RF subsystem.')
cwrRfBoardPartNumberClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrRfBoardPartNumberClass.setStatus('current')
if mibBuilder.loadTexts: cwrRfBoardPartNumberClass.setDescription('This object represents the board part number class of the RF subsystem.')
cwrRfBoardPartNumberBase = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrRfBoardPartNumberBase.setStatus('current')
if mibBuilder.loadTexts: cwrRfBoardPartNumberBase.setDescription('This object represents the board part number base of the RF subsystem.')
cwrRfBoardPartNumberVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrRfBoardPartNumberVersion.setStatus('current')
if mibBuilder.loadTexts: cwrRfBoardPartNumberVersion.setDescription('This object represents the board part number version of the RF subsystem.')
cwrRfBoardRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrRfBoardRevision.setStatus('current')
if mibBuilder.loadTexts: cwrRfBoardRevision.setDescription('This object represents the board revision of the RF subsystem.')
cwrRfSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrRfSerialNumber.setStatus('current')
if mibBuilder.loadTexts: cwrRfSerialNumber.setDescription('This object represents the serial number of the RF subsystem.')
cwrRfManfDate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 11), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrRfManfDate.setStatus('current')
if mibBuilder.loadTexts: cwrRfManfDate.setDescription('This object represents the manufacturing date of the RF subsystem.')
cwrRfVendorId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrRfVendorId.setStatus('current')
if mibBuilder.loadTexts: cwrRfVendorId.setDescription('This object represents the Radio frequency device vendor ID.')
cwrRfDuplexorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrRfDuplexorIndex.setStatus('current')
if mibBuilder.loadTexts: cwrRfDuplexorIndex.setDescription('This object represents the index into cwrDuplexorTable. This index identifies the Duplexor associated with this RF resource.')
cwrIntFreqEntityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2), )
if mibBuilder.loadTexts: cwrIntFreqEntityTable.setStatus('current')
if mibBuilder.loadTexts: cwrIntFreqEntityTable.setDescription('This table contains information about the intermediate frequency subsystem on the radio card.')
cwrIntFreqEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cwrIntFreqEntityEntry.setStatus('current')
if mibBuilder.loadTexts: cwrIntFreqEntityEntry.setDescription('This represents one entry in the cwrIntFreqEntityTable. This table is largely a read only table which provides details on the intermediate frequency subsystem available on the radio card. It is indexed by the ifIndex.')
cwrIfAssemblyPartNumberClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrIfAssemblyPartNumberClass.setStatus('current')
if mibBuilder.loadTexts: cwrIfAssemblyPartNumberClass.setDescription('This object represents the assembly part number class of the IF subsystem.')
cwrIfAssemblyPartNumberBase = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrIfAssemblyPartNumberBase.setStatus('current')
if mibBuilder.loadTexts: cwrIfAssemblyPartNumberBase.setDescription('This object represents the assembly part number base of the IF subsystem.')
cwrIfAssemblyPartNumberVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrIfAssemblyPartNumberVersion.setStatus('current')
if mibBuilder.loadTexts: cwrIfAssemblyPartNumberVersion.setDescription('This object represents the assembly part number version of the IF subsystem.')
cwrIfBoardPartNumberClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrIfBoardPartNumberClass.setStatus('current')
if mibBuilder.loadTexts: cwrIfBoardPartNumberClass.setDescription('This object represents the board part number class of the IF subsystem.')
cwrIfBoardPartNumberBase = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrIfBoardPartNumberBase.setStatus('current')
if mibBuilder.loadTexts: cwrIfBoardPartNumberBase.setDescription('This object represents the board part number base of the IF subsystem.')
cwrIfBoardPartNumberVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrIfBoardPartNumberVersion.setStatus('current')
if mibBuilder.loadTexts: cwrIfBoardPartNumberVersion.setDescription('This object represents the board part number version of the IF subsystem.')
cwrIfBoardRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrIfBoardRevision.setStatus('current')
if mibBuilder.loadTexts: cwrIfBoardRevision.setDescription('This object represents the board revision of the IF subsystem.')
cwrIfSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrIfSerialNumber.setStatus('current')
if mibBuilder.loadTexts: cwrIfSerialNumber.setDescription('This object represents the serial number of the IF subsystem.')
cwrIfManfDate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrIfManfDate.setStatus('current')
if mibBuilder.loadTexts: cwrIfManfDate.setDescription('This object represents the manufacturing date of the IF subsystem.')
cwrIfVendorId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrIfVendorId.setStatus('current')
if mibBuilder.loadTexts: cwrIfVendorId.setDescription('This object represents the IF vendor ID.')
cwrIfSwRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 1, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrIfSwRevision.setStatus('current')
if mibBuilder.loadTexts: cwrIfSwRevision.setDescription('This object represents the IF software revision.')
cwrImageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1), )
if mibBuilder.loadTexts: cwrImageTable.setStatus('current')
if mibBuilder.loadTexts: cwrImageTable.setDescription('This table provides facilities to manage the firmware images that the router will use to configure the radio line cards. When images need to be downloaded, the software will search this list starting from the first, for an image whose capabilities match the configuration specified in the cwrRadioBaseTable and the cwrRadioPhyTable and download that image to the appropriate hardware component. Insertion into the table at arbitrary points is not supported. Any new image URL added to this table will be inserted at index 1 only. Also note that an image gets downloaded to the hardware only when when a radio link is administratively enabled.')
cwrImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-WIRELESS-EXP-MIB", "cwrImageIndex"))
if mibBuilder.loadTexts: cwrImageEntry.setStatus('current')
if mibBuilder.loadTexts: cwrImageEntry.setDescription('This represents one entry in the cwrImageTable.')
cwrImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cwrImageIndex.setStatus('current')
if mibBuilder.loadTexts: cwrImageIndex.setDescription('This represents the one entry in this table. It also represents the search order. When images need to be downloaded to the hardware, the images are searched in the order of this index for an image that matches the hardware capabilities and uses it.')
cwrImageNameUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwrImageNameUrl.setStatus('current')
if mibBuilder.loadTexts: cwrImageNameUrl.setDescription('This object is the name of the image in the Universal Resource Locator (URL) format. This URL will be used to access the image when needed.')
cwrImageState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("imageInvalid", 1), ("imageValid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrImageState.setStatus('current')
if mibBuilder.loadTexts: cwrImageState.setDescription('This represents the state of the image. image_invalid(1): If the image could not be accessed for any reason. image_valid(2) : Image accessible and available for use.')
cwrImageSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrImageSize.setStatus('current')
if mibBuilder.loadTexts: cwrImageSize.setDescription('This represents the size of the image in bytes.')
cwrImageChipClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrImageChipClass.setStatus('current')
if mibBuilder.loadTexts: cwrImageChipClass.setDescription('This represents the class of chips onto which this image may be loaded.')
cwrImageChipType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrImageChipType.setStatus('current')
if mibBuilder.loadTexts: cwrImageChipType.setDescription('This represents the download method to use.')
cwrImageCapability1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrImageCapability1.setStatus('current')
if mibBuilder.loadTexts: cwrImageCapability1.setDescription('This represents a bitmask. The bit mask identifies the capabilities of this image. See also cwrImageCapability2.')
cwrImageCapability2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrImageCapability2.setStatus('current')
if mibBuilder.loadTexts: cwrImageCapability2.setDescription('This represents a bitmask. The bit mask identifies the capabilities of this image in addition to cwrImageCapability1.')
cwrImageVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrImageVersion.setStatus('current')
if mibBuilder.loadTexts: cwrImageVersion.setDescription('This represents the version number of this image.')
cwrImageTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrImageTag.setStatus('current')
if mibBuilder.loadTexts: cwrImageTag.setDescription('This object is the tag string associated with the image. Normally used to trace the source code used to generate this image.')
cwrImageOp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("nop", 0), ("add", 1), ("delete", 2), ("move", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwrImageOp.setStatus('current')
if mibBuilder.loadTexts: cwrImageOp.setDescription('This object represents the operation to be performed on the identified image. nop(0) - This value will be returned when this object is read. add(1) - Will add the image URL, as the first entry in the image table. delete(2) - Will delete the specified ULR from the image table. move(3) - Will make the image specified by the URL the first entry in the imageTable.')
cwrLedTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1), )
if mibBuilder.loadTexts: cwrLedTable.setStatus('current')
if mibBuilder.loadTexts: cwrLedTable.setDescription('Entity (Light emitting diode) LED information. For each LED on the entity, an entry will exist in this table, describing the location and current status of that LED.')
cwrLedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-WIRELESS-EXP-MIB", "cwrLedIndex"))
if mibBuilder.loadTexts: cwrLedEntry.setStatus('current')
if mibBuilder.loadTexts: cwrLedEntry.setDescription("An entry in the table, containing the LED information about the entity. The entPhysicalIndex identifies the entity on which the Led's are present.")
cwrLedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: cwrLedIndex.setStatus('current')
if mibBuilder.loadTexts: cwrLedIndex.setDescription('For a given entPhysicalIndex, this index value uniquely identifies an entry in the cwrLedTable.')
cwrLedName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrLedName.setStatus('current')
if mibBuilder.loadTexts: cwrLedName.setDescription('The label of the LED on the physical entity or a textual description to identify the usage of the LED.')
cwrLedVerticalPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrLedVerticalPosition.setStatus('current')
if mibBuilder.loadTexts: cwrLedVerticalPosition.setDescription('The position of the LED in the entity. It is counted from top to bottom.')
cwrLedHorizontalPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrLedHorizontalPosition.setStatus('current')
if mibBuilder.loadTexts: cwrLedHorizontalPosition.setDescription('The position of the LED in the entity. It is counted from from left to right.')
cwrLedMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("automatic", 1), ("latched", 2), ("forceOff", 3), ("forceSolidGreen", 4), ("forceSolidYellow", 5), ("forceBlinkGreen", 6), ("forceBlinkYellow", 7), ("forceBlinkBoth", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwrLedMode.setStatus('current')
if mibBuilder.loadTexts: cwrLedMode.setDescription('This objects specifies the desired mode of LED updates. automatic(1) and latched(2) are settings used by the software to determine how the LED should be updated. The others are for diagnostic purposes. The LED will be turned on or off as specified by the other (3-8) settings. The modes mean the following: automatic(1): The system updates the LED according to the default settings for that entity. latched(2): Once the LED is turned on, user has to turn it off. This applies only to alarm LEDs. forceOff(3): Force the LED off. forceSolidGreen(4): Force the LED to be solid green in on state. forceSolidYellow(5):Force the LED to be solid Yellow in on state forceBlinkGreen(6): Force the LED to blink in Green. forceBlinkYellow(7):Force the LED to blink in Yellow. forceBlinkBoth(8): Force the LED to blink Yellow and Green alternatively.')
cwrLedCurrentColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("green", 1), ("yellow", 2), ("blinkGreen", 3), ("blinkYellow", 4), ("blinkGreenYellow", 5), ("off", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwrLedCurrentColor.setStatus('current')
if mibBuilder.loadTexts: cwrLedCurrentColor.setDescription('Indicates the current color of the LED.')
cwrDuplexorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1), )
if mibBuilder.loadTexts: cwrDuplexorTable.setStatus('current')
if mibBuilder.loadTexts: cwrDuplexorTable.setDescription('This table contains information about the Duplexors available for use on the system.')
cwrDuplexorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WIRELESS-EXP-MIB", "cwrDuplexorIndex"))
if mibBuilder.loadTexts: cwrDuplexorEntry.setStatus('current')
if mibBuilder.loadTexts: cwrDuplexorEntry.setDescription('This represents one entry in the cwrDuplexorTable. This table provides details on the Duplexors available on the system. It is indexed by the ifIndex and cwrDuplexorIndex.')
cwrDuplexorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cwrDuplexorIndex.setStatus('current')
if mibBuilder.loadTexts: cwrDuplexorIndex.setDescription('This object represents the index of this entry in the cwrDuplexorTable.')
cwrDuplexorCiscoPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwrDuplexorCiscoPartNumber.setStatus('current')
if mibBuilder.loadTexts: cwrDuplexorCiscoPartNumber.setDescription('This object represents the Cisco part number for this Duplexor.')
cwrDuplexorLoPassbandRange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwrDuplexorLoPassbandRange.setStatus('current')
if mibBuilder.loadTexts: cwrDuplexorLoPassbandRange.setDescription('This object represents the low frequency range that this Duplexor will pass through without any attenuation. All low frequencies outside this range will be attenuated to a level such that an RF resource that uses this Duplexor will be unable to transmit or receive those frequencies.')
cwrDuplexorHiPassbandRange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwrDuplexorHiPassbandRange.setStatus('current')
if mibBuilder.loadTexts: cwrDuplexorHiPassbandRange.setDescription('This object represents the high frequency range that this Duplexor will pass through without any attenuation. All high frequencies outside this range will be attenuated to a level such that an RF resource that uses this Duplexor will be unable to transmit or receive those frequencies.')
cwrDuplexorReceivePassband = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("loPassband", 1), ("hiPassband", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwrDuplexorReceivePassband.setStatus('current')
if mibBuilder.loadTexts: cwrDuplexorReceivePassband.setDescription('This object indicates which of the two passbands are being used to receive transmissions. The RF Resource can receive on either of the duplexor passbands. loPassband(1) - The RF Resource is receiving on a frequency within the range identified by cwrDuplexorLoPassbandRange. hiPassband(2) - The RF Resource is receiving on a frequency within the range identified by cwrDuplexorHiPassbandRange.')
cwrDuplexorCLEICode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwrDuplexorCLEICode.setStatus('current')
if mibBuilder.loadTexts: cwrDuplexorCLEICode.setDescription('The CLEI code for this Duplexor.')
cwrDuplexorVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwrDuplexorVendorName.setStatus('current')
if mibBuilder.loadTexts: cwrDuplexorVendorName.setDescription('The Vendor Name for this Duplexor.')
cwrDuplexorSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 52, 1, 4, 1, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwrDuplexorSerialNumber.setStatus('current')
if mibBuilder.loadTexts: cwrDuplexorSerialNumber.setDescription('The Serial number of this Duplexor.')
cwrRadioExpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 52, 2))
cwrRadioExpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 1))
cwrRadioExpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 2))
cwrRadioExpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 1, 1)).setObjects(("CISCO-WIRELESS-EXP-MIB", "cwrComplianceRadioRFGroup"), ("CISCO-WIRELESS-EXP-MIB", "cwrComplianceRadioImageGroup"), ("CISCO-WIRELESS-EXP-MIB", "cwrComplianceRadioLEDGroup"), ("CISCO-WIRELESS-EXP-MIB", "cwrComplianceRadioDuplexorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwrRadioExpCompliance = cwrRadioExpCompliance.setStatus('current')
if mibBuilder.loadTexts: cwrRadioExpCompliance.setDescription('The compliance statement for Point to Point wireless interface devices compliant to Cisco Systems Inc. specification.')
cwrComplianceRadioRFGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 2, 1)).setObjects(("CISCO-WIRELESS-EXP-MIB", "cwrRfSwRevision"), ("CISCO-WIRELESS-EXP-MIB", "cwrRfAssemblyPartNumberClass"), ("CISCO-WIRELESS-EXP-MIB", "cwrRfAssemblyPartNumberBase"), ("CISCO-WIRELESS-EXP-MIB", "cwrRfAssemblyPartNumberVersion"), ("CISCO-WIRELESS-EXP-MIB", "cwrRfBoardPartNumberClass"), ("CISCO-WIRELESS-EXP-MIB", "cwrRfBoardPartNumberBase"), ("CISCO-WIRELESS-EXP-MIB", "cwrRfBoardPartNumberVersion"), ("CISCO-WIRELESS-EXP-MIB", "cwrRfBoardRevision"), ("CISCO-WIRELESS-EXP-MIB", "cwrRfSerialNumber"), ("CISCO-WIRELESS-EXP-MIB", "cwrRfManfDate"), ("CISCO-WIRELESS-EXP-MIB", "cwrRfVendorId"), ("CISCO-WIRELESS-EXP-MIB", "cwrRfDuplexorIndex"), ("CISCO-WIRELESS-EXP-MIB", "cwrIfAssemblyPartNumberClass"), ("CISCO-WIRELESS-EXP-MIB", "cwrIfAssemblyPartNumberBase"), ("CISCO-WIRELESS-EXP-MIB", "cwrIfAssemblyPartNumberVersion"), ("CISCO-WIRELESS-EXP-MIB", "cwrIfBoardPartNumberClass"), ("CISCO-WIRELESS-EXP-MIB", "cwrIfBoardPartNumberBase"), ("CISCO-WIRELESS-EXP-MIB", "cwrIfBoardPartNumberVersion"), ("CISCO-WIRELESS-EXP-MIB", "cwrIfBoardRevision"), ("CISCO-WIRELESS-EXP-MIB", "cwrIfSerialNumber"), ("CISCO-WIRELESS-EXP-MIB", "cwrIfManfDate"), ("CISCO-WIRELESS-EXP-MIB", "cwrIfVendorId"), ("CISCO-WIRELESS-EXP-MIB", "cwrIfSwRevision"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwrComplianceRadioRFGroup = cwrComplianceRadioRFGroup.setStatus('current')
if mibBuilder.loadTexts: cwrComplianceRadioRFGroup.setDescription('Group of objects implemented in the point to point wireless system for managing the Radio Frequency resources on the link.')
cwrComplianceRadioImageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 2, 2)).setObjects(("CISCO-WIRELESS-EXP-MIB", "cwrImageNameUrl"), ("CISCO-WIRELESS-EXP-MIB", "cwrImageState"), ("CISCO-WIRELESS-EXP-MIB", "cwrImageSize"), ("CISCO-WIRELESS-EXP-MIB", "cwrImageChipType"), ("CISCO-WIRELESS-EXP-MIB", "cwrImageChipClass"), ("CISCO-WIRELESS-EXP-MIB", "cwrImageCapability1"), ("CISCO-WIRELESS-EXP-MIB", "cwrImageCapability2"), ("CISCO-WIRELESS-EXP-MIB", "cwrImageVersion"), ("CISCO-WIRELESS-EXP-MIB", "cwrImageTag"), ("CISCO-WIRELESS-EXP-MIB", "cwrImageOp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwrComplianceRadioImageGroup = cwrComplianceRadioImageGroup.setStatus('current')
if mibBuilder.loadTexts: cwrComplianceRadioImageGroup.setDescription('Group of objects implemented in the point to point wireless system for managing images related to the point-to-point wireless firmware.')
cwrComplianceRadioLEDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 2, 3)).setObjects(("CISCO-WIRELESS-EXP-MIB", "cwrLedName"), ("CISCO-WIRELESS-EXP-MIB", "cwrLedVerticalPosition"), ("CISCO-WIRELESS-EXP-MIB", "cwrLedHorizontalPosition"), ("CISCO-WIRELESS-EXP-MIB", "cwrLedMode"), ("CISCO-WIRELESS-EXP-MIB", "cwrLedCurrentColor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwrComplianceRadioLEDGroup = cwrComplianceRadioLEDGroup.setStatus('current')
if mibBuilder.loadTexts: cwrComplianceRadioLEDGroup.setDescription('Group of objects implemented in the point to point wireless card to provide information about the LEDs on the card.')
cwrComplianceRadioDuplexorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 52, 2, 2, 4)).setObjects(("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorCiscoPartNumber"), ("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorLoPassbandRange"), ("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorHiPassbandRange"), ("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorReceivePassband"), ("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorCLEICode"), ("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorVendorName"), ("CISCO-WIRELESS-EXP-MIB", "cwrDuplexorSerialNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwrComplianceRadioDuplexorGroup = cwrComplianceRadioDuplexorGroup.setStatus('current')
if mibBuilder.loadTexts: cwrComplianceRadioDuplexorGroup.setDescription("Group of objects implemented in the point to point wireless card to provide information about the duplexor's in the system.")
mibBuilder.exportSymbols("CISCO-WIRELESS-EXP-MIB", cwrImageVersion=cwrImageVersion, cwrRadioFreqEntityGroup=cwrRadioFreqEntityGroup, cwrIfAssemblyPartNumberVersion=cwrIfAssemblyPartNumberVersion, cwrLedEntry=cwrLedEntry, cwrIfManfDate=cwrIfManfDate, cwrRfEntityIndex=cwrRfEntityIndex, ciscoWirelessExpMIB=ciscoWirelessExpMIB, cwrDuplexorHiPassbandRange=cwrDuplexorHiPassbandRange, cwrImageOp=cwrImageOp, cwrImageTable=cwrImageTable, cwrRadioImageGroup=cwrRadioImageGroup, cwrRfVendorId=cwrRfVendorId, cwrIfAssemblyPartNumberBase=cwrIfAssemblyPartNumberBase, cwrLedVerticalPosition=cwrLedVerticalPosition, cwrDuplexorEntry=cwrDuplexorEntry, cwrRfBoardRevision=cwrRfBoardRevision, cwrRadioDuplexorGroup=cwrRadioDuplexorGroup, cwrDuplexorCiscoPartNumber=cwrDuplexorCiscoPartNumber, cwrComplianceRadioLEDGroup=cwrComplianceRadioLEDGroup, cwrComplianceRadioDuplexorGroup=cwrComplianceRadioDuplexorGroup, cwrDuplexorLoPassbandRange=cwrDuplexorLoPassbandRange, cwrRfSwRevision=cwrRfSwRevision, cwrLedTable=cwrLedTable, cwrRadioExpConformance=cwrRadioExpConformance, cwrImageState=cwrImageState, cwrRadioExpCompliances=cwrRadioExpCompliances, cwrLedName=cwrLedName, cwrComplianceRadioRFGroup=cwrComplianceRadioRFGroup, cwrRadioExpCompliance=cwrRadioExpCompliance, cwrLedHorizontalPosition=cwrLedHorizontalPosition, cwrIfSerialNumber=cwrIfSerialNumber, cwrIfAssemblyPartNumberClass=cwrIfAssemblyPartNumberClass, cwrRfAssemblyPartNumberVersion=cwrRfAssemblyPartNumberVersion, cwrRfAssemblyPartNumberBase=cwrRfAssemblyPartNumberBase, cwrDuplexorTable=cwrDuplexorTable, cwrRadioLedGroup=cwrRadioLedGroup, cwrIfVendorId=cwrIfVendorId, cwrRfBoardPartNumberVersion=cwrRfBoardPartNumberVersion, cwrDuplexorCLEICode=cwrDuplexorCLEICode, cwrRadioExpMibObjects=cwrRadioExpMibObjects, cwrRfManfDate=cwrRfManfDate, cwrRfDuplexorIndex=cwrRfDuplexorIndex, cwrRadioExpGroups=cwrRadioExpGroups, cwrDuplexorReceivePassband=cwrDuplexorReceivePassband, cwrRfEntityEntry=cwrRfEntityEntry, cwrLedIndex=cwrLedIndex, cwrLedCurrentColor=cwrLedCurrentColor, cwrIntFreqEntityEntry=cwrIntFreqEntityEntry, cwrIfSwRevision=cwrIfSwRevision, cwrIntFreqEntityTable=cwrIntFreqEntityTable, cwrImageEntry=cwrImageEntry, cwrRfBoardPartNumberClass=cwrRfBoardPartNumberClass, cwrRfEntityTable=cwrRfEntityTable, cwrDuplexorVendorName=cwrDuplexorVendorName, cwrLedMode=cwrLedMode, cwrRfAssemblyPartNumberClass=cwrRfAssemblyPartNumberClass, cwrIfBoardPartNumberVersion=cwrIfBoardPartNumberVersion, cwrIfBoardRevision=cwrIfBoardRevision, cwrIfBoardPartNumberClass=cwrIfBoardPartNumberClass, cwrImageIndex=cwrImageIndex, cwrImageChipType=cwrImageChipType, cwrIfBoardPartNumberBase=cwrIfBoardPartNumberBase, cwrImageCapability1=cwrImageCapability1, cwrImageNameUrl=cwrImageNameUrl, cwrDuplexorIndex=cwrDuplexorIndex, cwrRfSerialNumber=cwrRfSerialNumber, cwrComplianceRadioImageGroup=cwrComplianceRadioImageGroup, cwrImageCapability2=cwrImageCapability2, cwrDuplexorSerialNumber=cwrDuplexorSerialNumber, cwrImageSize=cwrImageSize, PYSNMP_MODULE_ID=ciscoWirelessExpMIB, cwrImageChipClass=cwrImageChipClass, cwrImageTag=cwrImageTag, cwrRfBoardPartNumberBase=cwrRfBoardPartNumberBase)
