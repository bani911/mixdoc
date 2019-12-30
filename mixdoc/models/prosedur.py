# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class prosedur(models.Model):
    _name = 'prosedur'

    company_id = fields.Many2one('res.company', 'Organisasi', default=lambda self: self.env.user.company_id, readonly=True)
    no_prosedur = fields.Char(string="No.Prosedur", required=True)
    name = fields.Char(string="Nama Prosedur", required=True)
    tgl_terbit = fields.Date('Tgl Efektif', required=True)
    pemrakarsa = fields.Char(string="Pemrakarsa", required=True)
    keterangan = fields.Text('Keterangan')
    lampiran_prosedur = fields.Binary("Lampiran")
    doc_filename_prosedur = fields.Char("Filename Lampiran")
    # kirim_prosedur = fields.Many2one('pengiriman.prosedur', 'Pengiriman_Prosedur')
    # penerima = fields.Many2one('res.users', 'Diterima Oleh')
    # tgl_terima = fields.Date('Tgl Terima')
    item_list = fields.One2many('prosedur.item', 'list_id', 'Item List')

    _sql_constraints = [('cek_unik_nomor', 'UNIQUE(no_prosedur)', 'No.Prosedur tidak boleh sama!')]

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, rec.name + " - " + rec.no_prosedur))
        return res

class prosedur_item(models.Model):
    _name = 'prosedur.item'

    list_id = fields.Many2one('prosedur', 'Reference')
    no_dok = fields.Char('No.Dokumen', required=True)
    nama_dok = fields.Char('Nama Dokumen', required=True)
    tgl_efektif = fields.Date('Tgl Efektif', required=True)
