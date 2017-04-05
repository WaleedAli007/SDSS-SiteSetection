# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SiteRankingSDSS
                                 A QGIS plugin
 Generates a map to rank multiple alternatives priority wise
                             -------------------
        begin                : 2015-12-28
        copyright            : (C) 2015 by Waleed Ali
        email                : waleedali070@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SiteRankingSDSS class from file SiteRankingSDSS.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .SiteRankingSDSS import SiteRankingSDSS
    return SiteRankingSDSS(iface)
